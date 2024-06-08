import os, sys
import allure
import pytest
import requests
from utils import logger
from InterfaceTestConfig import readConfig

sys.path.append((os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))))


class WebAttack:
    def sql_injection(self, payload):
        url = readConfig.loginUrl
        data = {
            "staff_id": payload,
            "password": payload
        }
        h = {
            "Host": "101.34.99.21:3000",
            "Accept": "application/json, text/plain, */*",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0",
            "Content-Type": "application/x-www-form-urlencoded",
            "Origin": "http://rework.dfrobot.work",
            "Referer": "http://rework.dfrobot.work/",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6,en-GB;q=0.5",
            "Connection": "keep-alive"
        }
        try:
            response = requests.post(url, data=data, headers=h, timeout=10)
        except requests.exceptions.RequestException as e:
            logger.error(f"Request failed: {e}")
            pytest.fail("Request failed")

        logger.info(f"Testing SQL Injection with payload: {payload}")
        logger.info(f"Response Code: {response.status_code}")
        logger.info(f"response text:\n{response.text}")

        assert response.status_code != 200, "SQL Injection Detected"

    def xss(self, payload):
        url = readConfig.SearchUrl
        test_url = f"{url}?search={payload}"
        response = requests.get(test_url)
        logger.info(f"Testing XSS with payload: {payload}")
        logger.info(f"Response Code: {response.status_code}")
        logger.info(f"Response Text: {response.text}")

        assert response.status_code != 200, "Status code is 200"
        assert "XSS" not in response.text, "XSS detected"


    def csrf(self):
        url = readConfig.csrfUrl
        payload = {
            "age": "",
            "avatar_url": "https://offerzhip.cn/avatar_img/default_avatar.png",
            "edu": "0",
            "email": "",
            "gender": "0",
            "graduate_year": "",
            "intro": "",
            "is_bind_wechat": "1",
            "is_black": "",
            "major": "csrfAttack",
            "nickname": "微信用户779089",
            "phone": "******",
            "school": ""
        }
        headers = {
            "authority": "www.offershow.cn",
            "method": "POST",
            "path": "/api/od/update_person_info",
            "scheme": "https",
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6,en-GB;q=0.5",
            "Accesstoken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxMTI0NTY1m9zX3VZXJfaWQiOiAsInNIY29uZF91c2VyX2lkIjowLCJvc19yZWNvbW1lbmRlZF9pZCI6MCwiaXNmYWx1ZGkiOiAwLCwiaXNlbmNydXB0ZWRfaWQiOjAsImZhbGVfY29kZSI6MCwiZ3JhZGVfdGVzdCI6MCwiYXV0aG9yaXplZCI6MSwiaXNzIjoid3d3Lm9mZmVyc2hvdy5jbiIsImV4cCI6MTY4ODkyNjc2OX0.E0WAUtkMngqOYaqLboLba0WhMME4lV5erWK1_62XYbI",
            "Content-Type": "application/x-www-form-urlencoded",
            "Cookie": "Hm_lvt_8d190a6a8caef0302c52f5bd37e38f9b=1715668472,1717408949; _uvc_=CgxtazU0LWUyNzIxNDIxLWMzOTAtNGYzYi1hYzI5LTIxNDkwMTdmOGNlZQ%3D%3D; Hm_lpvt_8d190a6a8caef0302c52f5bd37e38f9b=1717408962",
            "Origin": "https://www.offershow.cn",
            "Priority": "u=1, i",

             # "Referer": "https://www.offershow.cn/account?type=1",

            "Referer": "http://www.evil.com",

            "Sec-Ch-Ua": "\"Microsoft Edge\";v=\"125\", \"Chromium\";v=\"125\", \".Not/A=Brand\";v=\"24\"",
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": "\"Windows\"",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0",
        }
        response = requests.post(url, data=payload, headers=headers)
        print(f"Testing CSRF with payload: {payload}")
        print(f"Response Code: {response.status_code}")
        print(f"Response Body: {response.text}")

        if response.status_code == 200 and "210001" in response.text.lower():
            print("Potential CSRF vulnerability detected.")
        else:
            print("CSRF protection is in place or request failed.")


    def post_sql_injection(self):
        url = "http://localhost:7777/updatePassword"  # 目标接口URL
        data = {
            "username": "admin' AND (SELECT COUNT(*) FROM user) > 0 -- ",
            "password": "123456"
        }
        headers = {
            "Host": "localhost:7777",
            "Accept": "application/json, text/plain, */*",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0",
            "Content-Type": "application/json",
            "Origin": "http://localhost:7777",
            "Referer": "http://localhost:7777/",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6,en-GB;q=0.5",
            "Connection": "keep-alive"
        }
        try:
            response = requests.post(url, json=data, headers=headers)
        except requests.exceptions.RequestException as e:
            logger.error(f"Request failed: {e}")
            pytest.fail("Request failed")

        logger.info(f"Testing SQL Injection with payload: admin' AND (SELECT COUNT(*) FROM inject) > 0 --")
        logger.info(f"Response Code: {response.status_code}")
        #此处预期，如果注入成功,将会收到springboot后台的输出
        logger.info(f"Response text:\n{response.text}")

        # 此处预期，如果注入成功，将会返回200状态码，因为(SELECT COUNT(*) FROM inject) > 0 为真
        assert response.status_code == 200, "SQL Injected fail"



