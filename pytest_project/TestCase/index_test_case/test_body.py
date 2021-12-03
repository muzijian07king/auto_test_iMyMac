import allure
import pytest
from pytest_project.common.readconfig import ini
from pytest_project.page_object.index.body_page import BodyPage
from pytest_project.common.readelement import Element, get_branch_all_keys
from pytest_project.config.conf import cm

body = Element('index/body')


@allure.feature("首页测试")
@allure.story("body内容测试")
class TestBody(object):
    @pytest.fixture(scope='function', autouse=True)
    def open_index(self, drivers):
        self.driver = BodyPage(drivers)
        self.driver.get_url(ini.url)

    @allure.title('测试轮播按钮')
    def test_001(self):
        """点击向左轮播图按钮"""
        allure.dynamic.tag('图片向右滚动')
        self.driver.click_carousel_left_button()
        assert self.driver.return_carousel_class() == 'item'

    @allure.title('测试轮播按钮')
    def test_002(self):
        """点击向右轮播图按钮"""
        allure.dynamic.tag('图片向左滚动')
        self.driver.click_carousel_right_button()
        assert self.driver.return_carousel_class() == 'item'

    @allure.title('测试下载ppm')
    @allure.severity('blocker')
    def test_003(self):
        """下载ppm"""
        allure.dynamic.tag('下载ppm')
        self.driver.click_ppm_download()
        assert 'dmg' in cm.get_download_filename() or 'crdownload' in cm.get_download_filename()

    @allure.severity('blocker')
    @allure.title('测试下载video')
    def test_004(self):
        """下载video"""
        allure.dynamic.tag('下载video')
        self.driver.click_carousel_right_button()
        self.driver.click_video_download()
        assert 'dmg' in cm.get_download_filename() or 'crdownload' in cm.get_download_filename() or 'pkg' in \
               cm.get_download_filename()

    @allure.title('测试ppm产品详情页面')
    @allure.severity('trivial')
    def test_005(self):
        """ppm产品详情页面"""
        allure.dynamic.tag('ppm产品页')
        self.driver.click_ppm_more()
        assert 'powermymac' in self.driver.get_current_url()

    @allure.title('测试video产品详情页面')
    @allure.severity('trivial')
    def test_006(self):
        """video产品详情页面"""
        allure.tag('video产品页')
        self.driver.click_carousel_right_button()
        self.driver.click_video_more()
        assert 'video' in self.driver.get_current_url()

    @pytest.mark.parametrize('link', get_branch_all_keys().get_branch_all_keys(body.data, 'featureItem'))
    @allure.severity('critical')
    def test_007(self, link):
        """点击功能介绍链接"""
        allure.dynamic.tag('{}功能页面'.format(link))
        allure.dynamic.title('点击{}链接'.format(link))
        self.driver.click_link(link)
        assert link in self.driver.get_current_url()

    @allure.title('测试轮播按钮')
    def test_008(self):
        """点击评价栏的轮播图左滑动按钮"""
        allure.dynamic.tag('图片向右滑动')
        self.driver.scroll_to_media()
        self.driver.click_media_left_button()
        assert self.driver.return_media_class() == 'item'

    @allure.title('测试轮播按钮')
    def test_009(self):
        """点击评价栏的轮播图右滑动按钮"""
        allure.dynamic.tag('图片向左滚动')
        self.driver.scroll_to_media()
        self.driver.click_media_right_button()
        assert self.driver.return_media_class() == 'item'

    @allure.title('测试介绍安全栏是否存在')
    @allure.severity('trivial')
    def test_010(self):
        """介绍栏是否存在"""
        allure.dynamic.tag('检查介绍栏')
        assert self.driver.return_container_whether_null()

    @allure.title('测试去顶部按钮')
    def test_011(self):
        """去顶部"""
        allure.dynamic.tag('回到顶部')
        self.driver.scroll_top()
        assert self.driver.return_whether_top()
