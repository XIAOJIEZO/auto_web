import pytest
import allure

from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from auto_web.pom.pages.adminLoginPage import AdminLoginPage
from auto_web.toolutils.get_test_data import GetTestData


@allure.story('管理后台用户登录')
class TestAdminLogin(object):
    data = GetTestData().get_json_data('AdminLogin.json', 'AdminLogin')

    @allure.title("{desp}")
    @pytest.mark.parametrize("url, username, pwd, captcha, expected, desp", data)
    def test_admin_login(self, driver, url, username, pwd, captcha, expected, desp):
        adminLoginPage = AdminLoginPage(driver)
        adminLoginPage.goto_login_page(url)
        adminLoginPage.input_username(username)
        adminLoginPage.input_pwd(pwd)
        adminLoginPage.input_captcha(captcha)
        adminLoginPage.click_login()

        if desp != '登录成功':
            WebDriverWait(driver, 5).until(EC.alert_is_present())
            alert = driver.switch_to.alert
            assert alert.text == expected
            alert.accept()
        else:
            WebDriverWait(driver, 5).until(EC.url_matches(r'/jpress/admin/index'))
            assert driver.title == expected
