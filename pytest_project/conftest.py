import os
import allure
import pytest

from py.xml import html
from selenium import webdriver
from pytest_project.utils.times import datetime_format
from pytest_project.config.conf import cm
from pytest_project.utils.sendemail import send_report
from pytest_project.utils.times import timestamp
import platform
from pytest_project.common.readconfig import ini

driver = None


@pytest.fixture(scope='session', autouse=True)
def drivers():
    """ 无头浏览器 """
    option = webdriver.ChromeOptions()
    option.add_argument('--headless')  # 无头显示
    option.add_argument('--window-size=1920,1080')
    option.add_argument('--no-sandbox')  # 设置浏览器大小
    option.add_argument('--incognito')
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    option.add_argument('ignore-certificate-errors')
    prefs = {'download.default_directory': cm.download_dir}  # 禁止图片
    option.add_experimental_option('prefs', prefs)
    global driver
    if driver is None:
        driver = webdriver.Chrome(options=option)
    yield driver
    driver.quit()


def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: list["Item"]
) -> None:
    # item表示每个测试用例，解决用例名称中文显示问题
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode-escape")
        item._nodeid = item._nodeid.encode("utf-8").decode("unicode-escape")
