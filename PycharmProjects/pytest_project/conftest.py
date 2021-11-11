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
    ''' 无头浏览器 '''
    option = webdriver.ChromeOptions()
    option.add_argument('--headless')
    option.add_argument('--window-size=1920,1080')
    prefs = {'download.default_directory': cm.download_dir}
    option.add_experimental_option('prefs', prefs)
    global driver
    if driver is None:
        driver = webdriver.Chrome(chrome_options=option)
    yield driver
    driver.quit()


# skips = ['skiprest_cleaner_menu', 'skiprest_cleaner_footbuy']
#
#
# def pytest_sessionstart(session):
#     session.failedmarkers = []
#     session.failednames = []


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    '''
    当测试失败的时候自动截图，展示到html报告中
    :param item:测试用例
    :return:
    '''
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    report.description = str(item.function.__doc__)
    extra = getattr(report, 'extra', [])
    """判断失败用例"""
    # if call.excinfo is not None:
    #     """获取pytest.mark的所有属性名称"""
    #     markers = [marker.name for marker in item.iter_markers()]
    #     for s in skips:
    #         if s in markers:
    #             item.session.failedmarkers.extend(markers)
    #             item.session.failedmarkers = list(set(item.session.failedmarkers))
    #             item.session.failednames.append(item.name.split('[')[0])
    if report.when == 'call' and report.failed:
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            screen_img = _capture_screenshot()
            if file_name:
                html = '<div><img src="data:image/png;base64,%s" alt="screenshot" style="width:1024px;height:768px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % screen_img
                extra.append(pytest_html.extras.html(html))
        report.extra = extra

        if hasattr(driver, "get_screenshot_as_png"):
            with allure.step('添加失败截图...'):
                allure.attach(driver.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)


# def pytest_runtest_setup(item):
#     markers = [marker.name for marker in item.iter_markers()]
#     if item.name.split('[')[0] in item.session.failednames:
#         for s in skips:
#             if s in markers:
#                 pytest.skip(f"previous test failed {item.name}")
#     for marker in markers:
#         if marker in item.session.failedmarkers:
#             for s in skips:
#                 if s in markers:
#                     pytest.skip(f"previous test failed {item.name}")


@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    cells.insert(1, html.th('用例名称'))
    cells.insert(2, html.th('Test_nodeid'))
    cells.pop(2)


# @pytest.mark.optionalhook
# def pytest_html_results_table_row(report, cells):
#     cells.insert(1, html.td(report.description))
#     cells.insert(2, html.td(report.nodeid))
#     cells.pop(2)


@pytest.mark.optionalhook
def pytest_html_results_table_html(report, data):
    if report.passed:
        del data[:]
        data.append(html.div('通过的用例未捕获日志输出.', class_='empty log'))


@pytest.mark.optionalhook
def pytest_html_report_title(report):
    html_time = datetime_format('%Y年%m月%d日')
    report.title = '{}测试报告'.format(html_time)


def pytest_configure(config):
    config._metadata.clear()
    config._metadata['测试项目'] = '测试IMAC官网'
    config._metadata['测试地址'] = ini.url
    config._metadata['Driver'] = 'Google'


def pytest_html_results_summary(prefix, summary, postfix):
    # prefix.clear()
    prefix.extend([html.p('所属部门：测试小组')])
    prefix.extend([html.p('测试执行人：李健')])


def pytest_terminal_summary(terminalreporter, exitstatus, config):
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
    # if result['failed'] or result['error']:
    #     send_report()


def pytest_collection_modifyitems(items):
    '''
    测试用例收集完成时，将收集到的item的name和nodeid的中文显示
    :param items:
    :return:
    '''
    for item in items:
        item.name = item.name.encode('utf-8').decode("unicode_escape")
        print(item.nodeid)
        item._nodeid = item.nodeid.encode('utf-8').decode("unicode_escape")


def _capture_screenshot():
    """截图保存为base64"""
    '''
       截图保存为base64
       :return:
       '''
    return driver.get_screenshot_as_base64()
