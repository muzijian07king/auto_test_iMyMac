import allure
import pytest

from pytest_project.common.readconfig import ini
from pytest_project.config.conf import cm

from pytest_project.page_object.index.head_page import HeadPage
from pytest_project.common.readelement import Element, get_recursion_key
from pytest_project.utils.logger import log

head = Element('index/head')


@allure.feature('首页测试')
@allure.story('导航栏测试')
class TestHead(object):
    @pytest.fixture(scope='function', autouse=True)
    @allure.step('打开谷歌浏览器进入官网')
    def open_index(self, drivers):
        self.driver = HeadPage(drivers)
        self.driver.get_url(ini.url)
        self.driver.click_sale_off_link()

    @allure.tag('链接测试')
    @pytest.mark.parametrize('link', get_recursion_key().get_recursion_key(head.data)[:6])
    @allure.severity('critical')
    def test_001(self, link):
        """点击网站logo链接"""
        self.driver.click_link(link)
        log.info('点击链接{}'.format(link))
        allure.dynamic.title('测试{}链接'.format(link))
        assert link.lower() in self.driver.get_current_url()

    @allure.tag('PowerMyMac下拉栏测试')
    @pytest.mark.parametrize('link', get_recursion_key().get_recursion_key(head.data)[8:13])
    @allure.severity('critical')
    def test_002(self, link):
        """点击PowerMyMac下拉框的链接"""
        allure.dynamic.title('测试{}链接'.format(link))
        self.driver.move_PowerMyMac_dropdown()
        log.info('点击PowerMyMac下拉框')
        self.driver.click_link(link)
        log.info('点击链接{}'.format(link))
        assert link.lower() in self.driver.get_current_url()

    @allure.tag('Online Tool下拉栏测试')
    @allure.severity('critical')
    @pytest.mark.parametrize('link', get_recursion_key().get_recursion_key(head.data)[13:17])
    def test_003(self, link):
        """点击Online Tool下拉框的链接"""
        allure.dynamic.title('测试{}链接'.format(link))
        self.driver.move_OnlineTools_dropdown()
        log.info('点击OnlineTool下拉框')
        self.driver.click_link(link)
        log.info('点击链接{}'.format(link))
        assert link.lower() in self.driver.get_current_url()

    @allure.tag('搜索文章')
    @allure.severity('critical')
    @pytest.mark.parametrize('text', ['Video', ' '])
    @pytest.mark.skipif(cm.VPN_Switch, reason='阿里云没有VPN')
    def test_004(self, text):
        """搜索栏输入关键字搜索测试"""
        allure.dynamic.title('测试输入{}关键字'.format(text))
        self.driver.click_search()
        log.info('点击搜索按钮')
        self.driver.send_search(text)
        log.info('输入关键字')
        self.driver.search_enter()
        log.info('按下回车')
        assert text.replace(' ', '+') in self.driver.get_current_url() \
               and text in self.driver.get_source
