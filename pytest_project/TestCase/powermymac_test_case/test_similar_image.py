import allure
import pytest

from pytest_project.common.readexcel import getExcelAllData
from pytest_project.page_object.powermymac.similar_page import SimilarPage
from pytest_project.common.readconfig import ini


@allure.severity('critical')
@allure.feature('PowerMyMac底部受欢迎功能介绍页面测试')
@allure.story('similar image页面内容测试')
class TestBody(object):

    @pytest.fixture(scope='function', autouse=True)
    def open_clear(self, drivers):
        self.driver = SimilarPage(drivers)
        self.driver.get_url(ini.get_url('similar-image'))

    @allure.title('container下载PowerMyMac测试')
    @allure.severity('blocker')
    def test_001(self):
        """下载PowerMyMac"""
        allure.dynamic.tag('下载PowerMyMac')
        self.driver.download_container_ppm()
        self.driver.assert_download()

    @allure.title("container进入powerMyMac购买页面测试")
    def test_002(self):
        """去powerMyMac购买页面"""
        allure.dynamic.tag("去购买PowerMyMac的网站")
        self.driver.goto_container_buy()
        self.driver.assert_go_buy()

    @allure.title('summary下载PowerMyMac测试')
    @allure.severity('blocker')
    def test_003(self):
        """下载PowerMyMac"""
        allure.dynamic.tag('下载PowerMyMac')
        self.driver.scroll_summary()
        self.driver.download_summary_ppm()
        self.driver.assert_download()

    @allure.title("summary进入powerMyMac购买页面测试")
    def test_004(self):
        """去powerMyMac购买页面"""
        allure.dynamic.tag("去购买PowerMyMac的网站")
        self.driver.scroll_summary()
        self.driver.goto_summary_buy()
        self.driver.assert_go_buy()

    @allure.title('测试navbar栏是否弹出')
    @allure.severity('blocker')
    def test_005(self):
        """弹出导航栏"""
        allure.dynamic.tag('弹出导航栏')
        self.driver.popup_nav()
        self.driver.assert_popup_nav()

    @allure.title('navbar下载PowerMyMac测试')
    @allure.severity('blocker')
    def test_006(self):
        """下载PowerMyMac"""
        allure.dynamic.tag('下载PowerMyMac')
        self.driver.popup_nav()
        self.driver.download_navbar_ppm()
        self.driver.assert_download()

    @allure.title("navbar进入powerMyMac购买页面测试")
    def test_007(self):
        """去powerMyMac购买页面"""
        allure.dynamic.tag("去购买PowerMyMac的网站")
        self.driver.popup_nav()
        self.driver.goto_navbar_buy()
        self.driver.assert_go_buy()

    @pytest.mark.parametrize('index,name,url', getExcelAllData('similar', 'pmm/common.xlsx'))
    def test_008(self, index, name, url):
        """进入技巧文章"""
        allure.dynamic.title(f'测试进入技巧文章：{name}')
        allure.dynamic.tag(f'{name}')
        self.driver.scroll_tip()
        self.driver.click_link(int(index), name)
        self.driver.assert_tip_html(url)

    @allure.title('测试进入index页面')
    @allure.tag('logo')
    def test_009(self):
        self.driver.popup_nav()
        self.driver.goto_index()
        self.driver.assert_index()
