#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
selenium基类
本文件存放了selenium基类的封装方法
"""
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import sys, os
import time

sys.path.append((os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))))

from config.conf import cm
from utils.times import sleep
from utils import logger

class WebPage(object):
    """selenium基类"""

    def __init__(self, driver):
        # self.driver = webdriver.Chrome()
        self.driver = driver
        self.timeout = 20
        self.wait = WebDriverWait(self.driver, self.timeout)

    def get_url(self, url):
        """打开网址并验证"""

        self.driver.set_page_load_timeout(60)
        try:
            self.driver.get(url)
            self.driver.implicitly_wait(10)
            logger.info("打开网页：%s" % url)
        except TimeoutException:
            raise TimeoutException("打开%s超时请检查网络或网址服务器" % url)

    @staticmethod
    def element_locator(func, locator):
        """元素定位器"""
        name, value = locator
        return func(cm.LOCATE_MODE[name], value)

    def find_element(self, locator):
        """寻找单个元素"""
        return WebPage.element_locator(lambda *args: self.wait.until(
            EC.presence_of_element_located(args)), locator)   # presence_of_element_located((By.ID,"id")) 显式等待

    def get_attrib(self, locator, value):
        """获取元素属性"""
        logger.info("获取属性")
        ele = self.find_element(locator)
        sleep(0.5)
        return ele.get_attribute(value)
        # js='document.querySelector("#质检表_返工单号").value'
        # self.driver.execute_script(js)

    def find_elements(self, locator):
        """查找多个相同的元素"""
        return WebPage.element_locator(lambda *args: self.wait.until(
            EC.presence_of_all_elements_located(args)), locator)

    def find_element_drag(self, locator):
        target = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)  # 拖动到可见的元素去

    def elements_num(self, locator):
        """获取相同元素的个数"""
        number = len(self.find_elements(locator))
        logger.info("相同元素：{}".format((locator, number)))
        return number

    def input_text(self, locator, txt):
        """输入(输入前先清空)"""
        sleep(0.5)
        ele = self.find_element(locator)
        ele.clear()
        ele.send_keys(txt)
        sleep(0.5)
        logger.info("输入文本：{}".format(txt))

    def input_enter(self, locator):
        """回车、tab等键入"""

        ele = self.find_element(locator)
        ele.send_keys(Keys.ENTER)

    def is_click(self, locator):
        """点击"""
        self.find_element(locator).click()
        sleep()
        logger.info("点击元素：{}".format(locator))

    def element_text(self, locator):
        """获取当前的text"""
        _text = self.find_element(locator).text
        logger.info("获取文本：{}".format(_text))
        return _text

    def hold_on(self, locator):
        # 定位到要悬停的元素
        move = self.find_element(locator)
        # 对定位到的元素执行悬停操作
        ActionChains(self.driver).move_to_element(move).perform()
        sleep()
        logger.info("悬停元素：{}".format(locator))

    def screen_scoll(self):
        self.driver.execute_script('window.scrollBy(0, 300)')
        sleep(1)

    @property
    def get_source(self):
        """获取页面源代码"""
        return self.driver.page_source

    def refresh(self):
        """刷新页面F5"""
        self.driver.refresh()
        self.driver.implicitly_wait(30)

    def switch_to_window(self, driver, winB):
        """
        :param winB:
            1.切换窗口的标题
            2.切换窗口的序号
            3.切换页面的元素
        :return: True 切换成功
        :Usage:
        1.
        driver.switch_to_window('win_name')
        2.
        driver.switch_to_window(2) # 切换到第二个窗口
        3.
        located=(By.ID,'id') # 确定切换页面的元素
        driver.switch_to_window(located) # 切换到页面中存在located的元素窗口
        """
        result = False
        handles = self.driver.window_handles
        current_handle = self.driver.current_window_handle
        if isinstance(winB, tuple):
            for handle in handles:
                self.driver.switch_to.window(handle)
                time.sleep(1)
                try:
                    self.driver.find_element(*winB)
                except NoSuchElementException:
                    pass
                else:
                    result = True
                    logger.info(f"切换到具有元素 {winB} 的窗口。")
                    break
            if not result:
                self.driver.switch_to.window(current_handle)
                time.sleep(2)
                logger.warn(f"未能切换到具有元素 {winB} 的窗口。")
        elif isinstance(winB, str):
            for handle in handles:
                self.driver.switch_to.window(handle)
                time.sleep(2)
                if winB in self.driver.title:
                    result = True
                    logger.info(f"切换到标题包含 '{winB}' 的窗口。")
                    break
            if not result:
                self.driver.switch_to.window(current_handle)
                time.sleep(2)
                logger.warn(f"未能切换到标题包含 '{winB}' 的窗口。")
        elif isinstance(winB, int):
            if winB <= len(handles):
                self.driver.switch_to.window(winB - 1)
                time.sleep(2)
                result = True
                logger.info(f"切换到第 {winB} 个窗口。")
        else:
            logger.error('无效的参数')
        return result
