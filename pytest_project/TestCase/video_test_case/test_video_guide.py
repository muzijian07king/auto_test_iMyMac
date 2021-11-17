import allure
import pytest

from pytest_project.page_object.video_converter.guide_page import GuidePage
from pytest_project.common.readconfig import ini
from pytest_project.common.readelement import Element, get_branch_all_keys

guide = Element('VideoConverter/video-guide')


@allure.severity('critical')
@allure.feature('VideoConverter页面测试')
@allure.story('Video-guide页面内容测试')
class TestBody(object):
    @pytest.fixture(scope='function', autouse=True)
    def open_clear(self, drivers):
        self.driver = GuidePage(drivers)
        self.driver.get_url(ini.get_url('video-guide'))
        self.driver.click_sale_off_link()

    @allure.severity('blocker')
    @allure.title('下载video测试')
    def test_001(self):
        """下载video功能测试"""
        allure.dynamic.tag('下载video')
        self.driver.click_download()
        assert self.driver.is_download()

    @allure.title('去订阅购买页面测试')
    def test_002(self):
        """去订阅购买页面功能测试"""
        allure.dynamic.tag('购买video')
        self.driver.goto_buy()
        assert self.driver.is_buy()

    @allure.severity('normal')
    @allure.title('去index页面测试')
    def test_003(self):
        """去index页面功能测试"""
        allure.dynamic.tag('index页面')
        self.driver.goto_index()
        assert self.driver.is_index()

    @allure.title('去guide页面测试')
    def test_004(self):
        """去guide页面功能测试"""
        allure.dynamic.tag('guide页面')
        self.driver.goto_guide()
        assert self.driver.is_guide()

    @allure.title('文章链接测试')
    @pytest.mark.parametrize('video_guide_article_name', get_branch_all_keys().get_branch_all_keys(guide.data, 'article-link'))
    def test_005(self, video_guide_article_name):
        """文章链接功能测试"""
        allure.dynamic.tag(video_guide_article_name)
        self.driver.scroll_to_article()
        self.driver.click_article(video_guide_article_name)
        assert self.driver.is_article(video_guide_article_name)