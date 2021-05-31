from PIL import Image
import pytesseract
import time
import base64
import requests
import urllib
import json


# 抠图
def cutout(driver, element):
    img1 = str(time.time()) + '.png'
    driver.save_screenshot(img1)

    # 左顶点坐标
    left = element.location['x']
    upper = element.location['y']
    # 右底点坐标
    right = element.size['width'] + left
    lower = element.size['height'] + upper

    # 抠图
    im = Image.open(img1)
    img = im.crop((left, upper, right, lower))
    img2 = str(time.time()) + '.png'
    img.save(img2)

    return img2


def get_simple_captcha(driver, element):
    # 返回captcha
    img = cutout(driver, element)
    captchaimg = Image.open(img)
    code = pytesseract.image_to_string(captchaimg)

    return code


def get_complex_captcha(driver, element):
    # api地址
    host = 'https://codevirify.market.alicloudapi.com'
    path = '/icredit_ai_image/verify_code/v1'
    url = host + path

    # 阿里云APPCODE
    appcode = 'c8d7424f4b454c138f97efdf7f072a7d'

    # 获取抠图
    img = cutout(driver, element)
    f = open(img, 'rb')
    contents = base64.b64encode(f.read())
    f.close()


    bodys = {}
    bodys['IMAGE'] = contents
    bodys['IMAGE_TYPE'] = '0'
    payload = urllib.parse.urlencode(bodys).encode('utf-8')
    request = urllib.request.Request(url, payload)

    request.add_header('Authorization', 'APPCODE ' + appcode)
    request.add_header('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8')

    response = urllib.request.urlopen(request)
    resp = json.loads(response.read())
    code = resp['VERIFY_CODE_ENTITY']['VERIFY_CODE']

    return code

