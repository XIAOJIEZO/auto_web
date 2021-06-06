from PIL import Image
import pytesseract
import time
import base64
from urllib import parse
from urllib import request
import json

# 抠图
def cutout(driver, *loc):
    element = driver.find_element(*loc)

    img1 = str(time.time()) + '.png'
    driver.save_screenshot(img1)

    # 左顶点坐标
    left = element.location['x']
    upper = element.location['y']
    # 右底点坐标
    right = element.size['width'] + left
    lower = element.size['height'] + upper

    # 抠图
    dpr = driver.execute_script('return window.devicePixelRatio')  # 屏幕缩放率
    im = Image.open(img1)
    img = im.crop((left * dpr, upper * dpr, right * dpr, lower * dpr))
    img2 = str(time.time()) + '.png'
    img.save(img2)

    return img2


def get_simple_captcha(driver, *loc):
    # 返回captcha
    img = cutout(driver, *loc)
    captchaimg = Image.open(img)
    code = pytesseract.image_to_string(captchaimg)

    return code


def get_complex_captcha(driver, *loc):
    # api地址
    host = 'https://codevirify.market.alicloudapi.com'
    path = '/icredit_ai_image/verify_code/v1'
    url = host + path

    # 阿里云APPCODE
    appcode = 'c8d7424f4b454c138f97efdf7f072a7d'

    # 获取抠图
    img = cutout(driver, *loc)
    f = open(img, 'rb')
    contents = base64.b64encode(f.read())
    f.close()

    bodys = {}
    bodys['IMAGE'] = contents
    bodys['IMAGE_TYPE'] = '0'
    payload = parse.urlencode(bodys).encode('utf-8')
    req = request.Request(url, payload)

    req.add_header('Authorization', 'APPCODE ' + appcode)
    req.add_header('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8')

    response = request.urlopen(req)
    resp = json.loads(response.read())
    captcha_code = resp['VERIFY_CODE_ENTITY']['VERIFY_CODE']

    return captcha_code
