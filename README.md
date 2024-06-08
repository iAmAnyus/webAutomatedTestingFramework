##                                               项目介绍

<p align=center>
   基于Python开发的Web自动化测试框架
</p>



<p align="center">
   <a target="_blank" href="https://github.com/iAmAnyus/webAutomatedTestingFramework">
      <img src="https://img.shields.io/badge/Python-3.10-blue"/>
      <img src="https://img.shields.io/badge/Selenium-4.20.0-green"/>
      <img src="https://img.shields.io/badge/Allure-2.11.0-yellow"/>
      <img src="https://img.shields.io/badge/Requests-2.20.0-red"/>
      <img src="https://img.shields.io/badge/Pytest-8.0.0-green"/>
   </a>
</p>


## 目录结构

```
automatedTestingFramework-master
├── allure-report         --  allure前端
├── allure-results        --  测试报告日志
├── UITestConfig          --  UI自动化配置模块
├── InterfaceTestConfig   --  接口自动化配置模块
├── page                  --  selenium封装模块
├── page_element          --  元素搜集模块
├── page_service          --  业务设计模块
├── script                --  脚本模块
├── test_case             --  测试用例模块
├── utils                 --  工具模块
├── report.html           --  pytest测试报告
├── pytest.ini            --  pytest配置文件
└── run_case.py           --  allure启动脚本
```
![image](https://github.com/iAmAnyus/webAutomatedTestingFramework/assets/130461533/4aeb8b57-c935-4b91-a0b7-eee7fd28e4d5)

## 项目特点

- **对Selenium库进行了二次封装**，使得测试人员可以更专注于测试场景的设计和执行，而不必过多关注底层细节。同时，具备了日志记录功能，可帮助测试人员更好地跟踪测试执行过程中的各种信息，提高故障排查效率。
- **模块化设计：** 受益于ORM框架思想，该项目将Web UI测试流程进行了分离解耦，提供了多个模块，使得测试人员可以根据需要选择性地使用不同的模块，从而更灵活地搭建测试流程，提高测试的可维护性和可扩展性。
- **多样例批量执行：** 通过集成pytest库，该项目实现了多样例批量执行，测试人员可以一次性运行多个测试用例，并通过pytest测试报告清晰地查看测试结果，提高测试效率和执行速度。
- **集成UI自动化测试与接口安全测试：** 项目支持UI自动化测试，同时集成了常用的API测试工具库Requests，实现了接口测试的自动化。此外，项目可选择引入安全测试样例，包括SQL注入、XSS、CSRF攻击等常见漏洞的检测，确保应用程序在功能测试和安全性方面都得到了全面覆盖。通过结合Selenium等Web Driver工具，测试人员可以在统一的平台上进行全面的测试，提高测试的覆盖率和深度。
- **UI可视化及数据分析：** 集成了Allure框架，该项目实现了自动化测试脚本的UI可视化，测试人员可以通过多种有助于数据分析的测试表格和统计图直观地查看测试结果，发现潜在的问题和趋势，从而及时采取措施提高被测试应用的质量。
- **基于Jenkins的CI/CD持续集成与交付：** 通过与Jenkins的集成，该项目可实现自动化构建和持续集成，框架可以在代码变更后自动触发测试任务，从而快速反馈和修复问题，进一步提高测试效率和项目的整体质量。

  
## 技术介绍

**技术栈：** Python、Selenium、Pytest、Allure、Jenkins、Requests

## 运行环境

Windows10、Python3.10

## 开发环境

| 开发工具 | 说明              |
| -------- | ----------------- |
| Pycharm  | Python开发工具IDE |

| 开发环境 | 版本   |
| -------- | ------ |
| Jdk      | 1.8    |
| Python   | 3.10.4 |
| Requests | 2.20.0 |
| Pytest   | 8.0.0  |
| Selenium | 4.20.0 |

## 模板样例及测试报告
### UI自动化模板样例
```python
# login2.yaml base on page_element 
登录按钮: 'xpath==//*[@id="s-top-loginbtn"]'
账号: 'xpath==//*[@id="TANGRAM__PSP_11__userName"]'
密码: 'xpath==//*[@id="TANGRAM__PSP_11__password"]'
协议: 'xpath==//*[@id="TANGRAM__PSP_11__isAgree"]'
登录: 'xpath==//*[@id="TANGRAM__PSP_11__submit"]'
新闻按钮: 'xpath==//*[@id="s-top-left"]/a[1]'
新闻页面标题: "百度新闻——海量中文资讯平台"
百度主页标题: "百度一下，你就知道"
登录错误: 'xpath==//*[@id="TANGRAM__PSP_11__error"]'

#readElement.py 元素搜集模块
class Element(object):
    """获取元素"""

    def __init__(self, name):
        self.file_name = '%s.yaml' % name
        self.element_path = os.path.join(cm.ELEMENT_PATH, self.file_name)
        if not os.path.exists(self.element_path):
            raise FileNotFoundError("%s 文件不存在！" % self.element_path)
        with open(self.element_path, encoding='utf-8') as f:
            self.data = yaml.safe_load(f)

    def __getitem__(self, item):
        """获取属性"""
        data = self.data.get(item)
        if data:
            name, value = data.split('==')
            return name, value
        raise ArithmeticError("{}中不存在关键字：{}".format(self.file_name, item))


#page.WebPage.py 业务设计模块
login = Element('login')  # 获取login.yaml
"""
login用法：
当调用login['名称']时会触发Element.__getitem__方法
return: Element类所读取的yaml元素配置文件相对应的键值
"""
class baiDuPage(WebPage):
    """
    登录
    """
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
        time.sleep(1)
        try:
           self.find_element(login['登录错误'])
           logger.error("登录失败：账号或密码错误")
           self.capture_screenshot("登录失败")
           pytest.fail("登录失败：账号或密码错误")
        except NoSuchElementException:
            pass
    """
    新闻
    """
    def btn_news(self):
        self.is_click(login['新闻按钮'])

# test_01.py 用例管理模块
@allure.story("测试样例1")
class Test01:
    @allure.step("初始化")
    @pytest.fixture(scope="function")
    def initialized(self, drivers):
        self.driver = baiDuPage(drivers)
        self.driver.get_url(ini.url)


    @allure.step("页面切换")
    @pytest.mark.usefixtures("initialized")
    def test_001(self):
        driver = self.driver
        driver.btn_news()
        time.sleep(1)
        driver.switch_to_window(driver, "百度一下，你就知道")


    @allure.step("测试用例2")
    def test_002(self):
        print("测试样例2")
        pass
```

### 接口安全测试模板样例

```python
#allure的测试接口配置
[url]
sampleUrl = https://www.baidu.com
loginUrl = http://rework.dfrobot.work/login
searchUrl = https://cs.swust.edu.cn/search
csrfUrl = https://www.offershow.cn/account?type=1


#readConfig.py 元素搜集模块
import os
import configparser
cur_path = os.path.dirname(os.path.realpath(__file__))
configPath = os.path.join(cur_path, "allureConf.ini")
conf = configparser.ConfigParser()

try:
    with open(configPath, 'r', encoding='utf-8') as config_file:
        conf.read_file(config_file)
except UnicodeDecodeError as e:
    print(f"Error reading configuration file: {e}")

"""readConfig.py中读取出来的allureConf.ini地址的传递给testcase"""
"""可在testcase中import此文件"""
"""适用于接口测试"""
# addUserUrl=conf.get("url","addUserUrl")
# loginUrl=conf.get("url","loginUrl")
# updateUserUrl=conf.get("url","updateUserUrl")
# deleteUserUrl=conf.get("url","deleteUserUrl")
# setUserPowerUrl=conf.get("url","setUserPowerUrl")
# exportUrl=conf.get("url","exportUrl")
loginUrl = conf.get("url","loginUrl")
SearchUrl = conf.get("url","SearchUrl")
csrfUrl = conf.get("url","csrfUrl")

#WebAttack.py 业务设计模块
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
   
#test_03.py 用例管理模块       
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
```

### Pytest测试报告
![image](https://github.com/iAmAnyus/webAutomatedTestingFramework/assets/130461533/e0c92d6e-3fe8-4246-b52e-8ffe93803c73)

### Allure可视化测试报告
![image](https://github.com/iAmAnyus/webAutomatedTestingFramework/assets/130461533/8bb2ace2-a7ea-4cdb-9b3d-b882a041370c)
![image](https://github.com/iAmAnyus/webAutomatedTestingFramework/assets/130461533/88a1a019-7cdb-4fea-bdc0-db52365557b4)


### 基于本地与线上的Jenkins的CI/CD持续集成
**参考：**

https://blog.csdn.net/weixin_57303037/article/details/135226326

https://www.cnblogs.com/luoshuai7394/p/17706998.html

**效果：**

![image](https://github.com/iAmAnyus/webAutomatedTestingFramework/assets/130461533/a89b6366-9aa8-439a-a6a8-118f33758757)
![image](https://github.com/iAmAnyus/webAutomatedTestingFramework/assets/130461533/ad9c5a55-e922-46ee-9ccc-ee5a28ca0289)
![image](https://github.com/iAmAnyus/webAutomatedTestingFramework/assets/130461533/18ab6c5a-839a-428d-a366-0a0e65e5bbfe)

## 快速开始
```cmd
in cmd
cd ./automatedTestingFramework-master
pip install -r requirements.txt

python run_case.py
```

## 项目待完成功能
部分Selenium方法的二次封装、测试数据持久化...
