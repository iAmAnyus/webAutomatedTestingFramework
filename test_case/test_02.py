# -*- coding:utf-8 -*-
import os, sys
import time

import allure

sys.path.append((os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))))

import pytest
from common.readConfig import ini
from page_service.login import baiDuPage


@allure.story("测试样例2")
class Test02:
    @allure.step("初始化")
    @pytest.fixture(scope="function")
    def initialized(self, drivers):
        self.login = baiDuPage(drivers)
        self.login.get_url(ini.url)

    @pytest.mark.usefixtures("initialized")
    @allure.step("登录且检测是否登录失败")
    def test_001(self):
        """
        登录
        """
        login = self.login
        login.BaiDuClick()
        login.protocol()
        login.input_user('yourUser')
        login.input_pwd('yourPwd')
        login.btn_login()
        time.sleep(1)

        # 判断是否登录失败,失败则截图并展示
        if login.is_login_failed():
            pytest.fail("登录失败：账号或密码错误")

    @pytest.mark.usefixtures("initialized")
    @allure.step("登录后的操作")
    def test_002(self):
        """
        登录后操作
        """
        time.sleep(1)
        print("登录后操作")
        pass

# pytest会自动搜索测试用例，不用在这里调用，这里只是为了单个文件调试的时候使用
# if __name__  == '__main__' :
#     pytest.main(['test_02.py','-s'])#'--capture=no'
