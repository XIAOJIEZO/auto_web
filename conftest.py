import pytest
from selenium import webdriver
import os


@pytest.fixture(scope='class')
def driver():
    return webdriver.Chrome()

# 检查screenshots文件夹知否存在
@pytest.fixture(scope='session', autouse=True)
def mkdir_screenshots():
    if not os.path.exists(r'screenshots'):
        os.mkdir('screenshots')
