# -*- coding:utf-8 -*-
import os, sys
import time
import allure
from UITestConfig.readConfig import ini
import pytest
from page_service.Interface.login import baiDuPage

sys.path.append((os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))))

@allure.story("测试用例1")
class Test01:
    @allure.step("初始化")
    @pytest.fixture(scope="function")
    def initialized(self, drivers):
        self.driver = baiDuPage(drivers)
        self.driver.get_url(ini.url)


    @allure.step("页面切换")
    @pytest.mark.usefixtures("initialized")
    def test_001(self):
        driver = self.driver
        driver.btn_news()
        time.sleep(1)
        driver.switch_to_window(driver, "百度一下，你就知道")


    @allure.step("step2")
    def test_002(self):
        print("step2")
        pass

# pytest会自动搜索测试用例，不用在这里调用，这里只是为了单个文件调试的时候使用
# if __name__  == '__main__' :
#     pytest.main(['test_01.py','-s'])#'--capture=no'
