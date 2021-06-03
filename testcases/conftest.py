import pytest
from selenium import webdriver

@pytest.fixture(scope='session')
def driver():
    driver = webdriver.Chrome()
    driver.get('')