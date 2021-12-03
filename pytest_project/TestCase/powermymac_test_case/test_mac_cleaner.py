import allure
import pytest

from pytest_project.page_object.powermymac.cleaner_page import CleanerPage
from pytest_project.common.readconfig import ini
from pytest_project.common.readelement import Element, get_branch_all_value, get_recursion_key

cleaner = Element('PowerMyMac/mac-cleaner')


@allure.feature('PowerMyMac下拉栏中页面测试')
@allure.story('mac-cleaner页面内容测试')
class TestBody(object):

    @pytest.fixture(scope='function', autouse=True)
    def open_clear(self, drivers):
        self.driver = CleanerPage(drivers)
        self.driver.get_url(ini.get_url('mac-cleaner'))

    @allure.severity('blocker')
    @allure.title('下载PowerMyMac测试')
    def test_001(self):
        """下载PowerMyMac"""
        allure.dynamic.tag('下载PowerMyMac')
        self.driver.download_mac_cleaner(cleaner['free-download'])
        assert self.driver.is_download()

    @allure.title("进入powerMyMac购买页面测试")
    @allure.severity('critical')
    def test_002(self):
        """去powerMyMac购买页面"""
        allure.dynamic.tag("去购买PowerMyMac的网站")
        self.driver.goto_buy(cleaner['buy'])
        assert self.driver.is_goto_buy()

    @allure.title("进入用户指南页面测试")
    @allure.severity('critical')
    def test_003(self):
        """去用户指南页面"""
        allure.dynamic.tag('去用户指南网站')
        self.driver.scroll_to_guide()
        self.driver.click_link(cleaner['guide'])
        assert self.driver.is_goto_guide()

    @allure.title('进入cleaner首页')
    def test_004(self):
        """去cleaner首页"""
        allure.dynamic.tag('去cleaner产品主页')
        self.driver.scroll_to_guide()
        self.driver.click_link(cleaner['mac-cleaner'])
        assert self.driver.is_cleaner_index()

    @allure.title('轮播图测试')
    def test_005(self):
        """点击轮播图索引图片是否变动"""
        allure.dynamic.tag('查看第二张轮播图')
        self.driver.scroll_to_carousel_comment()
        self.driver.click_carousel()
        assert self.driver.return_carousel_index()

    @allure.title('menu导航栏测试')
    @allure.severity('blocker')
    def test_006(self):
        """滑动到一定位置是否弹出menu"""
        allure.dynamic.tag('弹出menu导航栏')
        # self.driver.slide_in_driver(1100)
        self.driver.scroll_to_menu()
        assert self.driver.is_menu()

    @allure.title('menu导航栏下进入主页测试')
    @allure.severity('critical')
    def test_007(self):
        """点击menu下的主页链接"""
        allure.dynamic.tag('去cleaner产品主页')
        self.driver.scroll_to_menu()
        self.driver.click_link(get_branch_all_value().get_branch_all_value(cleaner.data, 'menu')[0])
        assert self.driver.is_cleaner_index()

    @allure.title('menu导航栏下进入用户指南页面测试')
    @allure.severity('critical')
    def test_008(self):
        """点击menu下的用户手册链接"""
        allure.dynamic.tag('去用户指南网站')
        self.driver.scroll_to_menu()
        self.driver.click_link(get_branch_all_value().get_branch_all_value(cleaner.data, 'menu')[1])
        assert self.driver.is_goto_guide()

    @allure.severity('blocker')
    @allure.title('menu导航栏cleaner的下载测试')
    def test_009(self):
        """点击menu下的下载链接"""
        allure.dynamic.tag('点击下载按钮')
        self.driver.scroll_to_menu()
        self.driver.download_mac_cleaner(get_branch_all_value().get_branch_all_value(cleaner.data, 'menu')[2])
        assert self.driver.is_download()

    @allure.title('menu导航栏下进入buy页面测试')
    @allure.severity('critical')
    def test_010(self):
        """点击menu导航栏下进入buy链接"""
        allure.dynamic.tag('点击buy按钮')
        self.driver.scroll_to_menu()
        self.driver.goto_buy(get_branch_all_value().get_branch_all_value(cleaner.data, 'menu')[3])
        assert self.driver.is_goto_buy()

    @allure.severity('blocker')
    @allure.title('footbuy导航栏cleaner的下载测试')
    def test_011(self):
        """点击footbuy下的下载链接"""
        allure.dynamic.tag('点击下载按钮')
        self.driver.scroll_to_footerBuy()
        self.driver.download_mac_cleaner(get_branch_all_value().get_branch_all_value(cleaner.data, 'footbuy')[0])
        assert self.driver.is_download()

    @allure.title('footbuy导航栏下进入buy页面测试')
    @allure.severity('critical')
    def test_012(self):
        """点击footbuy导航栏下进入buy链接"""
        allure.dynamic.tag('点击buy按钮')
        self.driver.scroll_to_footerBuy()
        self.driver.goto_buy(get_branch_all_value().get_branch_all_value(cleaner.data, 'footbuy')[1])
        assert self.driver.is_goto_buy()

    @allure.title('技巧栏链接测试')
    @allure.severity('critical')
    @pytest.mark.parametrize('link', get_recursion_key().get_recursion_key(cleaner.data)[4:8])
    def test_013(self, link):
        """点击技巧和窍门栏的链接"""
        allure.dynamic.tag('进入{}文章页面'.format(link))
        self.driver.scroll_to_container_text()
        self.driver.click_article_link(link)
        assert self.driver.is_goto_article(link)