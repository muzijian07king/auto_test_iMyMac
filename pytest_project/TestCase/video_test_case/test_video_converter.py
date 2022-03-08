import allure
import pytest

from pytest_project.page_object.video_converter.video_page import VideoPage
from pytest_project.common.readconfig import ini
from pytest_project.common.readexcel import getExcelAllData


@allure.severity('critical')
@allure.feature('VideoConverter页面测试')
@allure.story('VideoConverter主页内容测试')
class TestBody(object):
    @pytest.fixture(scope='function', autouse=True)
    def open_clear(self, drivers):
        self.driver = VideoPage(drivers)
        self.driver.get_url(ini.get_url('VideoConverter'))

    @allure.severity('blocker')
    @allure.title('切换win端测试')
    def test_001(self):
        """切换win端"""
        allure.dynamic.tag('切换win端')
        self.driver.switch_win()
        self.driver.assert_switch_win()

    @allure.severity('blocker')
    @allure.title('切换mac端测试')
    def test_002(self):
        """切换win端"""
        allure.dynamic.tag('切换mac端')
        self.driver.switch_mac()
        self.driver.assert_switch_mac()

    @allure.severity('blocker')
    @allure.title('下载win端iMyMac Video Converter测试')
    def test_003(self):
        """下载win端"""
        allure.dynamic.tag('下载win端')
        self.driver.switch_win()
        self.driver.download_video()
        self.driver.assert_download_win()

    @allure.severity('blocker')
    @allure.title('下载mac端iMyMac Video Converter测试')
    def test_004(self):
        """下载mac端"""
        allure.dynamic.tag('下载mac端')
        self.driver.switch_mac()
        self.driver.download_video()
        self.driver.assert_download_mac()

    @allure.severity('blocker')
    @allure.title('win选项跳转购买页面测试')
    def test_005(self):
        """跳转购买页面"""
        allure.dynamic.tag('跳转购买页面')
        self.driver.switch_win()
        self.driver.goto_buy()
        self.driver.assert_goto_buy()

    @allure.severity('blocker')
    @allure.title('mac选项跳转购买页面测试')
    def test_006(self):
        """跳转购买页面"""
        allure.dynamic.tag('跳转购买页面')
        self.driver.switch_mac()
        self.driver.goto_buy()
        self.driver.assert_goto_buy()

    @allure.severity('blocker')
    @pytest.mark.parametrize('index,name,url', getExcelAllData('video', 'Video/video.xlsx'))
    def test_007(self, index, name, url):
        """跳转技巧页面"""
        allure.dynamic.title(f'跳转技巧文章：{name}')
        allure.dynamic.tag(f'{name}')
        self.driver.scroll_tip()
        self.driver.click_tip_link(int(index), name)
        self.driver.assert_goto_tip(url)

    @allure.severity('blocker')
    @allure.title('导航栏点击logo测试')
    def test_008(self):
        """点击logo"""
        allure.dynamic.tag('点击logo')
        self.driver.popup_navbar()
        self.driver.click_logo()
        self.driver.assert_index()

    @allure.severity('blocker')
    @allure.title('导航栏下载win端iMyMac Video Converter测试')
    def test_009(self):
        """下载win端"""
        allure.dynamic.tag('下载win端')
        self.driver.switch_win()
        self.driver.popup_navbar()
        self.driver.click_download()
        self.driver.assert_download_win()

    @allure.severity('blocker')
    @allure.title('导航栏下载mac端iMyMac Video Converter测试')
    def test_010(self):
        """下载mac端"""
        allure.dynamic.tag('下载mac端')
        self.driver.switch_mac()
        self.driver.popup_navbar()
        self.driver.click_download()
        self.driver.assert_download_mac()

    @allure.severity('blocker')
    @allure.title('导航栏购买iMyMac Video Converter测试')
    def test_011(self):
        """购买iMyMac Video Converter"""
        allure.dynamic.tag('购买')
        self.driver.popup_navbar()
        self.driver.click_buy()
        self.driver.assert_goto_buy()
