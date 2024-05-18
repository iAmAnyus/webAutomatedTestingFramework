#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys, os
import time
sys.path.append((os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))))
from page.webPage import WebPage
from common.readElement import Element
login = Element('login')  # 获取login.yaml
"""
login用法：
当调用login['名称']时会触发Element.__getitem__方法
return: Element类所读取的yaml元素配置文件相对应的键值
"""
class baiDuPage(WebPage):

    """登录"""
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
    """
    新闻
    """
    def btn_news(self):
        self.is_click(login['新闻按钮'])


