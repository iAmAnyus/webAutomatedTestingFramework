#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
import sys
import subprocess

WIN = sys.platform.startswith('win')


def main():
   WIN = os.name == 'nt'

def run_tests():
    """
    运行测试并生成测试结果
    """
    activate_env = "venv\\Scripts\\activate" if WIN else "source venv/bin/activate"
    pytest_command = "pytest --alluredir=allure-results  --rootdir=UITestConfig"
    steps = [
        activate_env,
        pytest_command,
    ]

    for step in steps:
        subprocess.run("call " + step if WIN else step, shell=True)

def generate_and_open_allure_report():
    """
    生成并打开 Allure 报告
    """
    generate_command = "allure generate allure-results -o allure-report --clean"
    open_command = "allure open allure-report"

    steps = [
        generate_command,
        open_command,
    ]

    for step in steps:
        subprocess.run(step, shell=True)



if __name__ == "__main__":
   run_tests()
   generate_and_open_allure_report()
