import pytest
from selenium import webdriver


@pytest.fixture(scope='class')
def driver():
    return webdriver.Chrome()
