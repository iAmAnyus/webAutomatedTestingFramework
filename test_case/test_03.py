import os, sys
import allure
import pytest
from page_service.UI import WebAttack

sys.path.append((os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))))
attack = WebAttack.WebAttack()

@allure.story("Web攻击用例")
class Test03:
    @allure.step("SQL注入检测")
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

    @allure.step("XSS检测")
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

    @allure.step("CSRF检测")
    def test_csrf(self):
       """
       @function: 测试CSRF攻击
       """
       attack.csrf()

    @allure.step("Post型SQL注入检测")
    def test_post_sql_injection(self):
        """
        @function: 测试Post型SQL注入
        """
        attack.post_sql_injection()

    @allure.step("文件上传漏洞检测")
    @pytest.mark.parametrize("payload", [
        {
            "file": ("shell.php", b"<?php system($_GET['cmd']); ?>", "image/jpeg"),
            "expected_fail": False
        },
        {
            "file": ("../../etc/passwd", b"root:x:0:0:", "text/plain"),
            "expected_fail": True
        },
        {
            "file": ("test.php.jpg", b"malicious-content", "image/jpeg"),
            "expected_fail": False
        },
        {
            "file": (".htaccess", b"AddType application/x-httpd-php .jpg", "text/plain"),
            "expected_fail": True
        },
        {
            "file": ("large.bin", b"A" * 1024 * 1024 * 100, "application/octet-stream"),
            "expected_fail": True
        }
    ], ids=[
        "WebShell上传",
        "路径穿越攻击",
        "双重扩展名绕过",
        ".htaccess攻击",
        "超大文件DoS攻击"
    ])
    def test_vuln_upload_attacks(self, payload):
        """
        @function: 测试上传漏洞
        @param payload: 注入负载
        """
        attack.vuln_upload_attacks(payload)


# pytest会自动搜索测试用例，不用在这里调用，这里只是为了单个文件调试的时候使用
# if __name__  == '__main__' :
#     pytest.main(['test_03.py','-s'])#'--capture=no'


