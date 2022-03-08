import allure
import pytest
from pytest_project.common.readconfig import ini
from pytest_project.page_object.index.body_page import BodyPage
from pytest_project.common.readexcel import getExcelAllData


@allure.feature("首页测试")
@allure.severity('critical')
@allure.story("body内容测试")
class TestBody(object):
    @pytest.fixture(scope='function', autouse=True)
    def open_index(self, drivers):
        self.driver = BodyPage(drivers)
        self.driver.get_url(ini.url)

    @allure.severity('blocker')
    @allure.title('测试ppm下载按钮')
    def test_001(self):
        """点击ppm下载按钮"""
        allure.dynamic.tag('下载ppm软件')
        self.driver.click_ppm_download()
        self.driver.assert_download()

    @allure.severity('blocker')
    @allure.title('测试进入ppm详情页面')
    def test_002(self):
        """进入ppm详情页面"""
        allure.dynamic.tag('进入ppm详情页面')
        self.driver.click_ppm_more()
        self.driver.assert_more()

    @allure.title('测试进入媒体官网')
    @allure.severity('blocker')
    @pytest.mark.parametrize('media_name,url', getExcelAllData('媒体按钮对应的网站', 'index/index.xlsx'))
    def test_003(self, media_name, url):
        """进入媒体官网"""
        allure.dynamic.tag(f'进入{media_name}媒体官网')
        self.driver.click_media(media_name)
        self.driver.assert_media(url)

    @allure.severity('blocker')
    @allure.title('测试返回页面顶部按钮')
    def test_004(self):
        """返回页面顶部"""
        allure.dynamic.tag('返回页面顶部')
        self.driver.scroll_to_top()
        self.driver.assert_whether_top()
