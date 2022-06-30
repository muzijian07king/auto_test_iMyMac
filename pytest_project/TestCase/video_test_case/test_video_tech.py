import allure
import pytest

from pytest_project.page_object.video_converter.tech_page import TechPage
from pytest_project.common.readconfig import ini


@allure.severity('critical')
@allure.feature('VideoConverter页面测试')
@allure.story('Video-tech页面内容测试')
class TestBody(object):
    @pytest.fixture(scope='function', autouse=True)
    def open_clear(self, drivers):
        self.driver = TechPage(drivers)
        self.driver.get_url(ini.get_url('video-tech'))

    @allure.severity('blocker')
    @allure.title('下载video测试')
    def test_001(self, clear_download_dir):
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