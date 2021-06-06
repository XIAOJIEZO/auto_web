from auto_web.pom.pages.adminLoginPage import AdminLoginPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import allure
from time import sleep


@allure.story('用户登录')
class TestAdminLogin(object):
    data = [
        ['admin', 'admin', '666', '验证码不正确，请重新输入', '输入错误验证码'],
        ['', 'admin', '666', '账号不能为空', '账号为空'],

    ]

    @allure.title("{desp}")
    @pytest.mark.parametrize("username, pwd, captcha, expected, desp", data)
    def test_admin_login(self, driver, username, pwd, captcha, expected, desp):
        adminLoginPage = AdminLoginPage(driver)
        sleep(1)
        adminLoginPage.goto_login_page()
        sleep(1)

        adminLoginPage.input_username(username)
        sleep(1)
        adminLoginPage.input_pwd(pwd)
        sleep(1)
        adminLoginPage.input_captcha(captcha)
        sleep(1)
        adminLoginPage.click_login()
        sleep(1)

        if desp != '登录成功':
            WebDriverWait(driver, 5).until(EC.alert_is_present())
            alert = driver.switch_to.alert
            assert alert.text == expected
            alert.accept()

        else:
            WebDriverWait(driver, 5).until(EC.url_changes)
            assert driver.title == expected

        sleep(3)
