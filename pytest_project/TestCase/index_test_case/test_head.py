import allure
import pytest
from pytest_project.common.readconfig import ini
from pytest_project.config.conf import cm
from pytest_project.page_object.index.head_page import HeadPage
from pytest_project.common.readelement import Element

head = Element('index/head')


@allure.severity('blocker')
@allure.feature('首页测试')
@allure.story('导航栏测试')
class TestHead(object):
    @pytest.fixture(scope='function', autouse=True)
    @allure.step('打开谷歌浏览器进入官网')
    def open_index(self, drivers):
        self.driver = HeadPage(drivers)
        self.driver.get_url(ini.url)

    @allure.tag('右上角logo测试')
    @allure.severity('critical')
    def test_001(self):
        """点击网站logo链接"""
        self.driver.click_index_loge()
        allure.dynamic.title('跳转首页测试')
        self.driver.assert_index()

    @allure.tag('Utility栏链接测试')
    @pytest.mark.parametrize('link', list(head.readYaml('$.Utility').keys()))
    @allure.severity('critical')
    def test_002(self, link):
        """点击Utility的工具链接"""
        allure.dynamic.title('测试跳转{}产品页面'.format(link))
        self.driver.move_product_solution_dropdown()
        self.driver.click_utility(link)
        self.driver.assert_utility(link)

    @allure.tag('Online栏链接测试')
    @pytest.mark.parametrize('link', list(head.readYaml('$.Online').keys()))
    @allure.severity('critical')
    def test_003(self, link):
        """点击Online的工具链接"""
        allure.dynamic.title('测试跳转{}产品在线体验页面'.format(link))
        self.driver.move_product_solution_dropdown()
        self.driver.click_online(link)
        self.driver.assert_online(link)

    @allure.title('进入商店页面测试')
    @allure.tag('进入商店页面测试')
    @allure.severity('critical')
    def test_004(self):
        """点击Store"""
        self.driver.click_store()
        self.driver.assert_store()

    @allure.tag('进入帮助页面测试')
    @allure.severity('critical')
    def test_005(self):
        """点击Support"""
        allure.dynamic.title('进入帮助页面测试')
        self.driver.click_support()
        self.driver.assert_support()

    @allure.tag('搜索iMyMac上文章')
    @allure.severity('critical')
    @pytest.mark.parametrize('text', ['Video', ' '])
    @pytest.mark.skipif(cm.VPN_Switch, reason='阿里云没有VPN')
    def test_006(self, text):
        """搜索栏输入关键字搜索测试"""
        allure.dynamic.title('测试输入{}关键字'.format(text))
        self.driver.click_search()
        self.driver.send_search(text)
        self.driver.search_enter()
        self.driver.assert_search(text)

    @allure.tag('取消搜索iMyMac上文章')
    @allure.severity('normal')
    def test_007(self):
        """取消搜索iMyMac上文章"""
        allure.dynamic.title('取消搜索iMyMac上文章')
        self.driver.click_search()
        self.driver.close_search()
        self.driver.assert_close_search()
