import allure
import pytest

from pytest_project.page_object.video_converter.videopage import VideoPage
from pytest_project.common.readconfig import ini
from pytest_project.common.readelement import Element, get_branch_all_keys

video = Element('VideoConverter/body')


@allure.feature('VideoConverter页面测试')
@allure.story('VideoConverter主页内容测试')
class TestBody(object):
    @pytest.fixture(scope='function', autouse=True)
    def open_clear(self, drivers):
        self.driver = VideoPage(drivers)
        self.driver.get_url(ini.get_url('VideoConverter'))

    @allure.title('下载video测试')
    def test_001(self):
        """下载video功能测试"""
        allure.dynamic.tag('下载video')
        self.driver.download_video(video['free-download'])
        assert self.driver.is_download()

    @allure.title('去订阅购买页面测试')
    def test_002(self):
        """去订阅购买页面功能测试"""
        allure.dynamic.tag('购买video')
        self.driver.goto_buy(video['buy'])
        assert self.driver.is_goto_buy()

    @allure.title('conversion栏测试')
    def test_003(self):
        """conversion栏功能测试"""
        allure.dynamic.tag('conversion栏')
        self.driver.scroll_to_conversion()
        assert self.driver.return_conversion_handle()

    @allure.title('menu栏按钮测试')
    @pytest.mark.parametrize('i', list(range(5)))
    def test_004(self, i):
        """menu栏按钮功能测试"""
        allure.dynamic.tag('点击menu第{}个按钮'.format(i+1))
        self.driver.scroll_to_menu()
        self.driver.click_menu_button(i)
        assert self.driver.is_menu_skip_if(i)

    @allure.title('video编辑功能轮播图测试')
    @pytest.mark.parametrize('button_index', list(range(1, 10)))
    def test_005(self, button_index):
        """video编辑功能轮播图功能测试"""
        allure.dynamic.tag('点击编辑功能轮播图第{}个按钮'.format(button_index))
        self.driver.scroll_to_editing()
        self.driver.click_editing_button(button_index)
        assert self.driver.return_editing_image_class(button_index)

    @allure.title('文章链接测试')
    @pytest.mark.parametrize('video_article_name', get_branch_all_keys().get_branch_all_keys(video.data, 'article-link'))
    def test_006(self, video_article_name):
        """文章链接功能测试"""
        allure.dynamic.title('点击文章==》{}'.format(video_article_name))
        allure.dynamic.tag(video_article_name)
        self.driver.scroll_to_container_article()
        self.driver.click_container_link(video_article_name)
        assert self.driver.is_goto_article(video_article_name)

    @allure.title('enhancement栏测试')
    def test_007(self):
        """enhancement栏功能测试"""
        allure.dynamic.tag('enhancement栏')
        self.driver.scroll_to_container_enhancement()
        assert self.driver.return_container_enhancement_handle()

    @allure.title('评价轮播图测试')
    def test_008(self):
        """评价轮播图功能测试"""
        allure.dynamic.tag('评价轮播图')
        self.driver.scroll_to_carousel()
        self.driver.click_carousel()
        assert self.driver.return_carousel_index()
