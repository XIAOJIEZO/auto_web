import pytest
from selenium import webdriver
import os


@pytest.fixture(scope='class')
def driver():
    return webdriver.Chrome()
