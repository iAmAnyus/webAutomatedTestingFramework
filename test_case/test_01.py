# -*- coding:utf-8 -*-
import os, sys
import time
import allure
from common.readConfig import ini
import pytest
from page_service.login2 import baiDuPage

sys.path.append((os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))))

@allure.story("测试样例1")
class Test01:

    @allure.step("测试1.1")
    @pytest.fixture(scope="function")
    def test_001(self, drivers):
        driver = baiDuPage(drivers)
        driver.get_url(ini.url)
        driver.btn_news()
        time.sleep(1)
        driver.switch_to_window(drivers,"百度一下，你就知道")
        time.sleep(1)
        yield driver

    def test_002(self, test_001):
        pass

# pytest会自动搜索测试用例，不用在这里调用，这里只是为了单个文件调试的时候使用
# if __name__  == '__main__' :
#     pytest.main(['test_01.py','-s'])#'--capture=no'
