from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep

from auto_web.ToolsUtils.get_captcha import get_complex_captcha


class TestUserRegister(object):
    def __init__(self):
        # 打开谷歌浏览器
        self.driver = webdriver.Chrome()
        # 打开首页
        self.driver.get("http://localhost:8080/jpress/user/register")
        self.driver.maximize_window()

    def test_register_code_error(self):
        username = 'admin01'
        email = 'test01.qq.com'
        pwd = '123456'
        confirmPwd = '123456'
        captcha = 'xxxx'
        expected = '验证码不正确'

        self.driver.find_element(By.NAME, value='username').send_keys(username)
        self.driver.find_element(By.NAME, value='email').send_keys(email)
        self.driver.find_element(By.NAME, value='pwd').send_keys(pwd)
        self.driver.find_element(By.NAME, value='confirmPwd').send_keys(confirmPwd)
        self.driver.find_element(By.NAME, value='captcha').send_keys(captcha)
        self.driver.find_element(By.CLASS_NAME, value='btn').click()

        WebDriverWait(self.driver, 5).until(EC.alert_is_present())

        alert = self.driver.switch_to.alert

        assert alert.text == expected

        alert.accept()

    def test_register_ok(self):
        username = 'admin01'
        email = username + '@qq.com'
        pwd = '123456'
        confirmPwd = '123456'
        # 自动获取
        captcha = ''
        expected = '注册成功，点击确定进行登录。'

        # 输入用户名
        self.driver.find_element_by_name('username').clear()
        self.driver.find_element_by_name('username').send_keys(username)
        # email
        self.driver.find_element_by_name('email').clear()
        self.driver.find_element_by_name('email').send_keys(email)
        # 密码
        self.driver.find_element_by_name('pwd').clear()
        self.driver.find_element_by_name('pwd').send_keys(pwd)
        # 确认密码
        self.driver.find_element_by_name('confirmPwd').clear()
        self.driver.find_element_by_name('confirmPwd').send_keys(confirmPwd)

        # 输入验证码
        self.driver.find_element_by_name('captcha').clear()
        captcha = get_complex_captcha(self.driver, self.driver.find_element(By.XPATH, '//*[@id="captchaimg"]'))
        self.driver.find_element_by_name('captcha').send_keys(captcha)
        # 点击注册
        self.driver.find_element_by_class_name('btn').click()

        # 等待alert出现
        WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert

        # 验证
        assert alert.text == expected
        alert.accept()

        self.driver.close()
        self.driver.quit()

