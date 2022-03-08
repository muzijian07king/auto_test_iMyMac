import allure
import pytest

from pytest_project.page_object.video_converter.guide_page import GuidePage
from pytest_project.common.readconfig import ini
from pytest_project.common.readexcel import getExcelAllData


@allure.severity('critical')
@allure.feature('VideoConverter页面测试')
@allure.story('Video-guide页面内容测试')
class TestBody(object):
    @pytest.fixture(scope='function', autouse=True)
    def open_url(self, drivers):
        self.driver = GuidePage(drivers)
        self.driver.get_url(ini.get_url('video-guide'))

    @allure.severity('blocker')
    @allure.title('下载video测试')
    def test_001(self):
        """下载video功能测试"""
        allure.dynamic.tag('下载video')
        self.driver.click_download()
        self.driver.assert_download()

    @allure.title('去订阅购买页面测试')
    def test_002(self):
        """去订阅购买页面功能测试"""
        allure.dynamic.tag('购买video')
        self.driver.goto_buy()
        self.driver.assert_goto_buy()

    @allure.title('切换win指南测试')
    def test_003(self):
        """去index页面功能测试"""
        allure.dynamic.tag('win指南')
        self.driver.cut_win_guide()
        self.driver.assert_goto_win_guide()

    @allure.title('切换mac指南测试')
    def test_004(self):
        """去guide页面功能测试"""
        allure.dynamic.tag('mac指南')
        self.driver.cut_mac_guide()
        self.driver.assert_goto_mac_guide()

    @allure.title('指南跳转测试')
    @pytest.mark.parametrize('No, css', getExcelAllData('guide', 'Video/video.xlsx'))
    def test_005(self, No, css):
        """指南一跳转测试"""
        allure.dynamic.tag(No)
        self.driver.scroll_guide()
        self.driver.click_guide(No)
        self.driver.assert_goto_guide(css)
