#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys, os
import time
import pytest
from selenium.common import NoSuchElementException

sys.path.append((os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))))
from page.webPage import WebPage
from UITestConfig.readElement import Element
from utils import logger
login = Element('login')  # 获取login.yaml
"""
login用法：
当调用login['名称']时会触发Element.__getitem__方法
return: Element类所读取的yaml元素配置文件相对应的键值
"""
class baiDuPage(WebPage):
    """
    登录
    """
    def BaiDuClick(self):
        self.is_click(login['登录按钮'])

    def protocol(self):
        self.is_click(login['协议'])

    def input_user(self, content):
        self.input_text(login['账号'], content)

    def input_pwd(self, content):
        self.input_text(login['密码'], content)

    def btn_login(self):
        self.is_click(login['登录'])
        time.sleep(1)
        try:
           self.find_element(login['登录错误'])
           logger.error("登录失败：账号或密码错误")
           self.capture_screenshot("登录失败")
           pytest.fail("登录失败：账号或密码错误")
        except NoSuchElementException:
            pass
    """
    新闻
    """
    def btn_news(self):
        self.is_click(login['新闻按钮'])


