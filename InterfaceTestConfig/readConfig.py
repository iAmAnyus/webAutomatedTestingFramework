# coding:utf-8
import os
import configparser

cur_path=os.path.dirname(os.path.realpath(__file__))
configPath=os.path.join(cur_path, "allureConf.ini")
conf=configparser.ConfigParser()
conf.read(configPath)

"""readConfig.py中读取出来的allureConf.ini地址的传递给testcase"""
"""可在testcase中import此文件"""
"""适用于接口测试"""
# addUserUrl=conf.get("url","addUserUrl")
# loginUrl=conf.get("url","loginUrl")
# updateUserUrl=conf.get("url","updateUserUrl")
# deleteUserUrl=conf.get("url","deleteUserUrl")
# setUserPowerUrl=conf.get("url","setUserPowerUrl")
# exportUrl=conf.get("url","exportUrl")
