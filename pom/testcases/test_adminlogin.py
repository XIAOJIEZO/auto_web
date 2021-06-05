from auto_web.pom.pages.adminLoginPage import AdminLoginPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from time import sleep


class TestAdminLogin(object):
    data = [
        ['admin', 'admin', '666', '验证码不正确，请重新输入'],
        ['', 'admin', '666', '账号不能为空'],
        ['admin', 'admin', '', 'JPress后台']
    ]

    @pytest.mark.parametrize("username, pwd, captcha, expected", data)
    def test_admin_login(self, driver, username, pwd, captcha, expected):
        adminLoginPage = AdminLoginPage(driver)
        adminLoginPage.goto_login_page()
        adminLoginPage.input_username(username)
        adminLoginPage.input_pwd(pwd)
        adminLoginPage.input_captcha(captcha)
        adminLoginPage.click_login()
        sleep(3)

        if captcha == '666':
            WebDriverWait(driver, 5).until(EC.alert_is_present)
            alert = driver.switch_to.alert
            alert.text == expected
            assert alert.text == expected
            alert.accept()
        else:
            WebDriverWait(driver, 5).until(EC.title_is(expected))
            assert driver.title == expected

        sleep(3)