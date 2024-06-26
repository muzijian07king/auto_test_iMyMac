import allure
import pytest
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from pytest_project.utils.tool import if_port_hold, if_connect_google_200
from pytest_project.clear_download_dir import Clear
from pytest_project.config.conf import cm
from pytest_project.utils.times import timestamp
from pytest_project.utils.logger import Log
log = Log().get_log()
driver = None


@pytest.fixture(scope='session', autouse=True)
def drivers():
    """ 无头浏览器 """
    option = webdriver.ChromeOptions()
    option.add_argument('--headless')  # 无头显示
    option.add_argument('--window-size=1920,1080')  # 设置浏览器大小
    option.add_argument("--start-maximized")
    option.add_argument('--no-sandbox')  # 设置禁止沙盒模式
    option.add_argument('--incognito')  # 隐私模式启动
    if if_port_hold(7890):
        if if_connect_google_200:
            option.add_argument('--proxy-server=127.0.0.1:7890')  # 设置代理
            log.info('设置代理成功')
        else:
            log.info('设置代理失败')
    option.add_argument('--disable-gpu')   # 关闭gpu加速
    option.add_argument('--keep-alive-for-test')  # 热启动
    prefs = {'download.default_directory': cm.download_dir, 'excludeSwitches': ['enable-automation']}  # 设置下载路径
    option.add_experimental_option('prefs', prefs)
    option.add_argument('ignore-certificate-errors')
    global driver
    if driver is None:
        driver = webdriver.Chrome(options=option)
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
    当测试失败的时候自动截图，展示到allure报告中
    :param item:测试用例
    :return:
    """
    outcome = yield
    report = outcome.get_result()
    """判断失败用例"""
    if report.failed:
        if report.when == 'call' or report.when == 'teardown':
            if hasattr(driver, "get_screenshot_as_png"):
                with allure.step('添加失败截图...'):
                    try:
                        allure.attach(driver.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)
                    except TimeoutException:
                        log.error('截图失败')
                        allure.attach("截图失败，看日志", "失败截图", allure.attachment_type.TEXT)


def pytest_terminal_summary(terminalreporter):
    """收集测试结果"""
    result = {
        "total": terminalreporter._numcollected,
        'passed': len(terminalreporter.stats.get('passed', [])),
        'failed': len(terminalreporter.stats.get('failed', [])),
        'error': len(terminalreporter.stats.get('error', [])),
        'skipped': len(terminalreporter.stats.get('skipped', [])),
        # terminalreporter._sessionstarttime 会话开始时间
        'total times': timestamp() - terminalreporter._sessionstarttime
    }
    print(result)


def pytest_collection_modifyitems(items) -> None:
    # item表示每个测试用例，解决日志用例名称中文显示问题
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode-escape")
        item._nodeid = item._nodeid.encode("utf-8").decode("unicode-escape")


@pytest.fixture(scope='function')
def clear_download_dir():
    yield
    Clear().clear_download_files()

