from auto_web.pom.pages.UserLoginPage import UserLoginPage
from auto_web.toolutils.get_test_data import GetTestData
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import pytest
import allure


@allure.story("用户登录")
class TestUserLogin(object):
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.userLoginPage = UserLoginPage(self.driver)

    def teardown_class(self):
        self.driver.quit()

    data = GetTestData().get_json_data('UserLogin.json', 'UserLogin')

    @pytest.mark.parametrize("url,name,pwd,expected,desp", data)
    @allure.title("{desp}")
    def test_user_login(self, url, name, pwd, expected, desp):
        '''
        用例步骤：1.输入用户名 2.输入密码  3.点击登录
        '''
        self.userLoginPage.goto_page(url)
        with allure.step("输入用户名：" + name):
            self.userLoginPage.input_name(name)

        with allure.step("输入密码：" + pwd):
            self.userLoginPage.input_pwd(pwd)

        with allure.step("点击登录"):
            self.userLoginPage.click_login()

        if desp != '登录成功':
            WebDriverWait(self.driver, 5).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            assert alert.text == expected
            alert.accept()
        else:
            WebDriverWait(self.driver, 5).until(EC.url_matches(r"jpress/ucenter"))
            assert self.driver.title == expected

    @allure.title("跳转注册页面")
    def test_jump_register(self):
        self.driver.back()
        WebDriverWait(self.driver, 5).until(EC.url_matches(r"/jpress/user/login"))
        self.userLoginPage.jump_register()
        WebDriverWait(self.driver, 5).until(EC.url_matches(r"/jpress/user/register"))
        assert self.driver.title == "用户注册"
