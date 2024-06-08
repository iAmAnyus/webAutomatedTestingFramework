import os, sys
import allure
import pytest
from page_service import WebAttack

sys.path.append((os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))))
attack = WebAttack.WebAttack()

@allure.story("Web攻击用例")
class Test03:
    @allure.step("SQL注入测试")
    @pytest.mark.parametrize("payload", [
        "' OR '1'='1",
        "' OR '1'='1' -- ",
        "' OR '1'='1' /*",
        "' OR '1'='1' #",
        "' OR '1'='1' or ''='"
    ], ids=[
        "sql注入1",
        "sql注入2",
        "sql注入3",
        "sql注入4",
        "sql注入5"
    ])
    def test_sql_injection(self, payload):
        """
        @function: 测试SQL注入
        @param payload: 注入负载
        """
        attack.sql_injection(payload)

    @allure.step("XSS测试")
    @pytest.mark.parametrize("payload", [
        "<script>alert('XSS1')</script>",
        "'; alert('XSS2');",
        "\" onmouseover=\"alert('XSS3')\"",
        "<img src=x onerror=alert('XSS4')>",
        "<svg onload=alert('XSS5')>"
    ], ids=[
        "xss注入1",
        "xss注入2",
        "xss注入3",
        "xss注入4",
        "xss注入5"
    ])
    def test_xss(self, payload):
        """
        @function: 测试XSS注入
        @param payload: 注入负载
        """
        attack.xss(payload)


    def test_csrf(self):
       """
       @function: 测试CSRF攻击
       """
       attack.csrf()

    @allure.step("Post型SQL注入")
    def test_post_sql_injection(self):
        """
        @function: 测试Post型SQL注入
        """
        attack.post_sql_injection()


# pytest会自动搜索测试用例，不用在这里调用，这里只是为了单个文件调试的时候使用
# if __name__  == '__main__' :
#     pytest.main(['test_03.py','-s'])#'--capture=no'


