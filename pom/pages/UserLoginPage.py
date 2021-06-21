from selenium.webdriver.common.by import By
from auto_web.toolutils.basepage import BasePage
import allure


class UserLoginPage(BasePage):
    __name_input = (By.NAME, 'user')
    __pwd_input = (By.NAME, 'pwd')
    __login_btn = (By.CLASS_NAME, 'btn')
    __register_link = (By.XPATH, '/html/body/div/div/div/form/div[3]/div/p/a')

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def goto_login_page(self, url):
        self.goto_page(url)

    def input_name(self, text):
        self.input_text(text, *self.__name_input)

    def input_pwd(self, text):
        self.input_text(text, *self.__pwd_input)

    def click_login(self):
        self.click(*self.__login_btn)

    def jump_register(self):
        self.click(*self.__register_link)
