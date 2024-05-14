# -*- coding:utf-8 -*-
import os, sys
import time

import allure

sys.path.append((os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))))

import pytest
from common.readConfig import ini
from page_service.login2 import baiDuPage
from script import inspect

@allure.story("测试样例2")
class Test02:

    @allure.step("登录")
    @pytest.fixture(scope="function")
    def test_001(self, drivers):
        """登录"""
        login = baiDuPage(drivers)
        login.get_url(ini.url)
        login.BaiDuClick()
        login.protocol()
        login.input_user('yourUser')
        login.input_pwd('yourPwd')
        login.btn_login()
        time.sleep(3)
        yield login

    @allure.step("登录后的操作")
    @pytest.mark.usefixtures("test_001")
    def test_002(self, test_001):
        """登录后操作"""
        time.sleep(1)
        print("登录后操作")
        pass

# pytest会自动搜索测试用例，不用在这里调用，这里只是为了单个文件调试的时候使用
# if __name__  == '__main__' :
#     pytest.main(['test_02.py','-s'])#'--capture=no'
