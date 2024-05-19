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
├── common                --  公共方法模块
├── config                --  配置模块
├── page                  --  selenium封装模块
├── page_element          --  元素搜集模块
├── page_service          --  业务设计模块
├── script                --  脚本模块
├── test_case             --  测试用例模块
├── utils                 --  工具模块
├── conftest.py           --  pytest配置文件
├── pytest.ini            --  pytest日志配置文件
├── report.html           --  pytest测试报告
└── run_case.py           --  allure启动脚本
```

## 项目特点

- **对Selenium库进行了二次封装**，使得测试人员可以更专注于测试场景的设计和执行，而不必过多关注底层细节。同时，具备了日志记录功能，可帮助测试人员更好地跟踪测试执行过程中的各种信息，提高故障排查效率。
- **模块化设计：** 受益于ORM框架思想，该项目将Web UI测试流程进行了分离解耦，提供了多个模块，使得测试人员可以根据需要选择性地使用不同的模块，从而更灵活地搭建测试流程，提高了测试的可维护性和可扩展性。
- **多样例批量执行：** 通过集成pytest库，该项目实现了多样例批量执行，测试人员可以一次性运行多个测试用例，并通过pytest测试报告清晰地查看测试结果，提高了测试效率和执行速度。
- **UI可视化及数据分析：** 集成了Allure框架，该项目实现了自动化测试脚本的UI可视化，测试人员可以通过多种有助于数据分析的测试表格和统计图直观地查看测试结果，发现潜在的问题和趋势，从而及时采取措施提高被测试应用的质量。
- **基于Jenkins的CI/CD持续集成与交付：** 通过与Jenkins的集成，该项目可实现自动化构建和持续集成，测试人员可以在代码变更后自动触发测试任务，从而快速反馈和修复问题，进一步提高了测试效率和项目的整体质量。
## 技术介绍

**技术栈：** Python、Selenium、Pytest、Allure、Jenkins

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
### 模板样例
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

# page_Service base on page.WebPage.py(Selenium二次开发基类)
login = Element('login2')  # 获取login2.yaml
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

# test_case.test01 base on page_service.login2.py
class Test01:

    @allure.step("测试1.1")
    @pytest.fixture(scope="function")
    def test_001(self, drivers):
        driver = baiDuPage(drivers)
        driver.get_url(ini.url)
        driver.btn_news()
        time.sleep(1)
        driver.switch_to_window(drivers,"百度一下，你就知道")
        time.sleep(1)
        yield driver

    def test_002(self, test_001):
        pass

# test_case.test02 base on page_service.login2.py
@allure.story("测试样例2")
class Test02:

    @allure.step("登录")
    @pytest.fixture(scope="function")
    def test_001(self, drivers):
        """登录"""
        login = baiDuPage(drivers)
        login.get_url(ini.url)
        login.BaiDuClick()
        login.protocol()
        login.input_user('yourUser')
        login.input_pwd('yourPwd')
        login.btn_login()
        time.sleep(3)
        yield login

    @allure.step("登录后的操作")
    @pytest.mark.usefixtures("test_001")
    def test_002(self, test_001):
        """登录后操作"""
        time.sleep(1)
        print("登录后操作")
        pass
```
### Pytest测试报告
![image](https://github.com/iAmAnyus/webAutomatedTestingFramework/assets/130461533/9fe28d7b-8c7b-49c9-94cc-965db04f79ea)

### Allure可视化测试报告
![image](https://github.com/iAmAnyus/webAutomatedTestingFramework/assets/130461533/05699adf-7b48-4a6f-bde9-214b84a0c0a9)
![image](https://github.com/iAmAnyus/webAutomatedTestingFramework/assets/130461533/4442d5f6-87a6-4fca-a5c2-b44596907482)

### 基于本地与线上的Jenkins的CI/CD持续集成
**参考：**

https://blog.csdn.net/weixin_57303037/article/details/135226326

https://www.cnblogs.com/luoshuai7394/p/17706998.html

**效果：**

![image](https://github.com/iAmAnyus/webAutomatedTestingFramework/assets/130461533/a89b6366-9aa8-439a-a6a8-118f33758757)
![image](https://github.com/iAmAnyus/webAutomatedTestingFramework/assets/130461533/ad9c5a55-e922-46ee-9ccc-ee5a28ca0289)
![image](https://github.com/iAmAnyus/webAutomatedTestingFramework/assets/130461533/18ab6c5a-839a-428d-a366-0a0e65e5bbfe)

## 项目待完成功能
部分Selenium方法的二次封装、测试数据的持久化...
