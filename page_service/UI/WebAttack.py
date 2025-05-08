import os, sys
from pathlib import Path

import chardet
import allure
import pytest
import requests
from aiohttp import payload

from utils import logger
from InterfaceTestConfig import readConfig

sys.path.append((os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))))


class WebAttack:
    # 成功接口
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

        assert response.status_code == 401, "SQL Injection Detected"

    def xss(self, payload):
        url = readConfig.SearchUrl
        params = {
            "query": payload,
            "type": "article"
        }
        response = requests.get(url, params=params)
        assert payload not in response.text, f"XSS vulnerability detected with payload: {payload}"

        print(f"Tested payload: {payload}")
        print(f"Response status code: {response.status_code}")
        print(f"Response content: {response.text[:200]}...")  # 只打印前 200 个字符


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
            "path": "/api/od/update_full_person_info",
            "scheme": "https",
            "accept": "application/json, text/plain, */*",
            "Accept-encoding": "gzip, deflate, br, zstd",
            "Accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6,en-GB;q=0.5",
            "Accesstoken": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MTM3MjM3NiwidXVpZCI6Ijg2YmMxNzQ3LTJlOTYtNDIxNi05OGMyLTI2NGM3YmE5NzhiMyIsInNlY29uZF9pZCI6LTEwLCJzZWNvbmRfdXVpZCI6bnVsbCwibmlja25hbWUiOiJcdTVmYWVcdTRmZTFcdTc1MjhcdTYyMzc3NzkwODkiLCJ1bmlvbl9pZCI6Im9oTkxtczRUZkt6ZnhVQ3BmOEpGTDVvQlJGcHciLCJsZXZlbCI6MywiaWRlbnRpdHlfaW5mbyI6eyJlZHVjYXRpb24iOjAsInR5cGVfaWRlbnRpdHkiOm51bGwsInVzZXJfbGV2ZWwiOjMsInNjaG9vbF9hdXRoX3N0YXR1cyI6ZmFsc2UsImNvbXBhbnlfYXV0aF9zdGF0dXMiOmZhbHNlLCJzY2hvb2xfc3Rhcl9zdGF0dXMiOmZhbHNlLCJjb21wYW55X3N0YXJfc3RhdHVzIjpmYWxzZSwiX2xldmVsIjozfSwidmVyc2lvbiI6MSwiZXhwIjoxNzQ3MjgwNzgwLCJvcmlnX2lhdCI6MTc0NjcwNDc4MCwicmVmcmVzaF9hdCI6MTc0OTI2Nzk4MH0.7uZZj_UaehljTXgSvp7aRnaaMwpd4riFKBCNn8OsjeQ",
            "Content-type": "application/x-www-form-urlencoded",
            "Cookie": "uvc_=cGxtazU0LTQ4ZTQ2OThkLWNlMzYtNGUyZC1hZTg5LWU1ODczNjhhYWIyNg%3D%3D; Hm_lvt_8d190a6a8caef0302c52f5bd37e38f9b=1745487181,1745500123,1746172901,1746675966; HMACCOUNT=2F2543A10D604A5C; Hm_lpvt_8d190a6a8caef0302c52f5bd37e38f9b=1746676863",
            "Priority": "u=1, i",

            # "Referer": "https://www.offershow.cn/account?type=1",

            "Referer": "http://www.evil.com",


            "Sec-ch-ua": "\"Not(A:Brand\";v=\"99\", \"Microsoft Edge\";v=\"133\", \"Chromium\";v=\"133\"",
            "Sec-ch-ua-mobile": "?0",
            "Sec-ch-ua-platform": "\"Windows\"",
            "Sec-fetch-dest": "empty",
            "Sec-fetch-mode": "cors",
            "Sec-fetch-site": "same-origin",
            "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0"
        }
        response = requests.post(url, data=payload, headers=headers)
        print(f"Testing CSRF with payload: {payload}")
        print(f"Response Code: {response.status_code}")
        print(f"Response Body: {response.text}")

        if response.status_code == 200 and "210001" in response.text.lower():
            print("Potential CSRF vulnerability detected.")
        else:
            print("CSRF protection is in place or request failed.")

        assert response.status_code != 200 and response.json()["code"] != "210001", "CSRF Detected"

    # 失败接口
    def post_sql_injection(self):
        url = "http://localhost:7777/updatePassword"  # 目标接口URL
        data = {
            "username": "admin' AND (SELECT COUNT(*) FROM user) > 0 -- ",
            "password": "1234567"
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
        assert response.status_code != 200, "SQL Injected detected"

    def vuln_upload_attacks(self, payload):
        VULN_ENDPOINT = f"{readConfig.fileUploadUrl}/vuln/upload"

        # 从payload直接获取文件参数
        filename, content, mime_type = payload["file"]

        # 内存方式构造请求
        files = {'file': (filename, content, mime_type)}
        response = requests.post(VULN_ENDPOINT, files=files)
        encoding = chardet.detect(response.content)["encoding"]
        response.encoding = encoding

        print(f"[DEBUG] 响应状态码: {response.status_code}")
        print(f"[DEBUG] 响应内容: {response.text}")

        if payload["expected_fail"]:
            allure.dynamic.tag("防御验证")
            assert "文件上传成功" not in response.text, "接口意外允许危险文件上传"
        else:
            allure.dynamic.tag("漏洞检测")
            assert "文件上传成功" in response.text, "接口未返回成功标识"

            # # 路径检查（动态获取项目路径）
            # project_root = Path(__file__).parent.parent.parent
            # expected_file = project_root / "src/main/java/com/Anyus/files" / filename
            # assert expected_file.exists(), f"文件未存储到预期位置: {expected_file}"




