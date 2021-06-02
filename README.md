## selenium定位方法
```
# id
element = driver.find_element_by_id('kw')

# name
element = driver.find_element_by_name('kw')

# xpath
element = driver.find_element_by_xpath('//*[@id="kw"]')

# css_selector
element = driver.find_element_by_css_selector('#kw')

# class_name
element = find_element_by_class_name('s_ipt')

# link_text
element = driver.find_element_by_link_text('百度热搜')

# partial_link_text
element = find_element_by_partial_link_text('首页')

# tag_name
element = find_element_by_tag_name('input')[0]

# 综合的一种方法，优先使用ID定位
from selenium.webdriver.common.by import By
# self.driver.find_element(value='kw').send_keys('selenium')
self.driver.find_element(By.ID, value='kw').send_keys('selenium')
```

## selenium webdriver属性
```
# 浏览器名称
driver.name

# 当前url
driver.current_url

# 当前页面title
driver.title

# 当前页面源码
self.driver.page_source

# 窗口句柄
self.driver.current_window_handle

# 当前窗口所有句柄
self.driver.window_handles
```

## selenium webdriver方法
```
# 浏览器后退
driver.back()

# 浏览器前进
driver.forward()

# 浏览器刷新
driver.refresh()

# 关闭当前窗口
driver.close()

# 退出浏览器
driver.quit()

# 切换到frame
driver.switch_to.frame()

# 切换的alter
driver.switch_to.alert()

# 截屏
driver.save_screenshot('filename.png')

切换到活动元素
driver.switch_to_active.element()
```

## Selenium WebElement属性
```
element = self.driver.find_element_by_xpath('//*[@id="su"]')

# 表示
element.id

# 宽高
element.size

# 宽高和坐标
element.rect

# 坐标
element.location

# 标签名称
element.tag_name

# 文本内容
element.text
```

## Selenium WebElement方法
```
element = self.driver.find_element_by_xpath('//*[@id="su"]')

# 输入内容
element.send_keys('keys')
 
 # 点击
element.click()

# 清楚内容
element.clear()

# 截屏
element.screenshot('filename')

# 获取属性值
element.get_attribute()

# 是否可用
element.is_enabled()

# 是否被选中
element.is_selected()

# 是否显示
element.is_displayed()

# css属性值
element.value_of_css_property()
```

## form表单测试流程
- 1、定位表单元素
- 2、输入测试值
- 3、判断表单元素属性
- 4、获取表单元素属性
- 5、提交表单进行验证

## checkbox和radiobutton
- checkbox：1、如果checkbox有id属性可以直接使用id定位，如果没有可以通过input标签定位，然后通过type属性过滤（直接xpath定位不香吗）；
  2、选择或者反选，使用click()方法。
  
- radiobutton：radiobutton有相同的名称，多个值，可以先通过名称获得，然后通过值判断；2、选择或者反选，使用click()方法；3、唯一性。

## select
- 处理下拉列表，需要用到selenium中的一个工具类。
```
from selenium.webdriver.support.select import Select

se = self.driver.find_element(By.ID, value='s1')
select = Select(se)

# 根据值选择
select.select_by_value('47')

# 根据根据索引选择
select.select_by_index(1)

# 根据文本选择
select.select_by_visible_text('Mail')

# 根据值反选
select.deselect_by_value('47')

# 根据根据索引反选
select.deselect_by_index(1)

# 根据文本反选
select.deselect_by_visible_text('Mail')

# 反选全部(多选使用)
select.deselect_all

# 所有选项
options = select.options
for i in options:
print(i.text)

# 当前被选中所有选项
a = select.all_selected_options

# 第一个被选中选项
a = select.first_selected_option
```

## 页面弹窗处理
- 页面上的弹窗有三种：alter（用于提示）、confirm（用于确认）、prompt（输入内容）
```
# alert
alert = self.driver.switch_to.alert
alert.accept()  # 接受

# confirm
alert = self.driver.switch_to.alert
alert.accept()  # 接受
alert.dismiss() # 取消

# prompt
alert = self.driver.switch_to.alert
alert.send_keys('anything')
alert.accept()  # 接受
alert.dismiss() # 取消
```

## selenium的三种等待方式：在UI自动化测试的中，必然会遇到环境不稳定，网络慢的情况，这时不做任何处理的话，代码会由于没有找到页面元素儿报错。
- time.sleep():调试时使用，做测试不建议使用。会严重浪费资源
- 隐式等待：设置一个最长等待时间，如果在规定时间内网页加载完成，则执行下一步，否则一直等到时间结束；隐式等待对整个driver周期都起作用，在最开始设置一次就可以了。（弊端：JavaScript一般都是放在body后面加载，在等待的时候页面元素其实已经加载完了）
```
self.driver.implicitly_wait(10)
```
- 显示式待：直到某条件满足，推荐使用
```
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(self.driver, 10)
wait.until(EC.title_is('百度一下，你就知道')) 

# selenium等待条件
title_is  # 判断title是否出现
...
```

## selenium鼠标和键盘事件
```
from selenium.webdriver import ActionChains

mouse = ActionChains(self.driver)

# 单击鼠标左键
mouse.click_and_hold(element=None).perform()

# 单击鼠标左键，不松开
mouse.click_and_hold(element=None).perform()

# 单击鼠标右键
mouse.context_click(element=None).perform()

# 双击鼠标左键
mouse.double_click(element=None).perform()

# 移动鼠标到某个元素
mouse.move_to_element(to_element).perform()

# 某个坐标
mouse.move_by_offset(xoffset, yoffset).perform()

# 键盘操作
element.send_keys(Keys.CONTROL + 'a')
element = self.driver.find_element(By.XPATH, value='/html/body/form/input[3]')
element.send_keys('String')
element.send_keys(Keys.CONTROL + 'a')
```

## selenium执行Javascript脚本
```
js = "alert('text')"
# 同步执行
self.driver.execute_script(js)

# 异步执行
self.driver.execute_async_script(js)
```

## selenium定位frame
- frame标签有frameset、frame、iframe，frameset和其他普通标签没有区别，后两者需要特殊操作
```
# 切换frame
driver.switch_to.frame(frame_reference)

# 返回主文档
driver.switch_to_default.content()
```

## 获取图形验证码
- 网页验证码解决思路：1、截取整个页面；2、获得验证码坐标数据；3、根据坐标抠图；4、使用pytesseract模块进行验证。
