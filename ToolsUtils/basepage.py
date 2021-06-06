class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

        # 元素定位
        self.find_element = lambda *loc: self.driver.find_element(*loc)

        # 获取页面title
        self.page_title = lambda: self.driver.title

    def input_text(self, text, *loc):
        self.find_element(*loc).clear()
        self.find_element(*loc).send_keys(text)

    def click(self, *loc):
        self.find_element(*loc).click()