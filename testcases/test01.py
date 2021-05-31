from selenium import webdriver
from tools.get_captcha import get_simple_captcha
from tools.get_captcha import get_complex_captcha

class TestCase(object):
    def test_01(self):
        # 打开谷歌浏览器
        driver = webdriver.Chrome()
        # 打开首页
        driver.get("http://localhost:8080/jpress/user/register")
        driver.maximize_window()

        # 获取验证码图片

        element = driver.find_element_by_id("captchaimg")
        code = get_complex_captcha(driver=driver, element=element)
