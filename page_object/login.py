#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys, os

sys.path.append((os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))))

from page.webPage import WebPage
from common.readElement import Element

login = Element('login')  # 获取login.yaml


class LoginPage(WebPage):
    '''登录'''

    def input_user(self, content):
        self.input_text(login['账号'], content)

    def input_pwd(self, content):
        self.input_text(login['密码'], content)

    def btn_login(self):
        self.is_click(login['登录'])
