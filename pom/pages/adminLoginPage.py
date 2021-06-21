from selenium.webdriver.common.by import By
from auto_web.toolutils.basepage import BasePage
from auto_web.toolutils.get_captcha import get_complex_captcha


class AdminLoginPage(BasePage):
    __username_input = (By.NAME, 'user')
    __pwd_input = (By.NAME, 'pwd')
    __captcha_input = (By.NAME, 'captcha')
    __login_btn = (By.CLASS_NAME, 'btn')
    __captcha_img = (By.ID, 'captchaImg')

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def goto_login_page(self, url):
        self.goto_page(url)

    def input_username(self, username):
        self.input_text(username, *self.__username_input)

    def input_pwd(self, pwd):
        self.input_text(pwd, *self.__pwd_input)

    def input_captcha(self, captcha):
        if captcha == '666':
            self.input_text(captcha, *self.__captcha_input)
        else:
            code = get_complex_captcha(self.driver, *self.__captcha_img)
            self.input_text(code, *self.__captcha_input)

    def click_login(self):
        self.click(*self.__login_btn)
