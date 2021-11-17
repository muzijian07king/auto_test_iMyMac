import allure
import pytest

from pytest_project.page_object.sitemap.sitemap_page import SitemapPage
from pytest_project.common.readconfig import ini
from pytest_project.common.readelement import Element, get_branch_all_keys

sitemap = Element('SiteMap/siteMap')


@allure.feature('网址地图页面测试')
@allure.story('功能测试')
class TestBody(object):
    @pytest.fixture(scope='function', autouse=True)
    def open_url(self, drivers):
        self.driver = SitemapPage(drivers)
        self.driver.get_url(ini.get_url('sitemap'))
        self.driver.click_sale_off_link()

    @allure.title('PowerMyMac热门文章链接测试')
    @pytest.mark.parametrize('number', list(range(4)))
    def test_001(self, number):
        allure.dynamic.tag('热点为T{}的文章'.format(number % 4))
        title = self.driver.get_articles_title(number)
        self.driver.go_to_articles(number)
        assert self.driver.if_true_articles(title)

    @allure.title('Mac Cleaner热门文章链接测试')
    @pytest.mark.parametrize('number', list(range(4, 8)))
    def test_002(self, number):
        allure.dynamic.tag('热点为T{}的文章'.format(number % 4))
        title = self.driver.get_articles_title(number)
        self.driver.go_to_articles(number)
        assert self.driver.if_true_articles(title)

    @allure.title('File Shredder热门文章链接测试')
    @pytest.mark.parametrize('number', list(range(8, 12)))
    def test_003(self, number):
        allure.dynamic.tag('热点为T{}的文章'.format(number % 4))
        title = self.driver.get_articles_title(number)
        self.driver.go_to_articles(number)
        assert self.driver.if_true_articles(title)

    @allure.title('Duplicate Finder热门文章链接测试')
    @pytest.mark.parametrize('number', list(range(12, 16)))
    def test_004(self, number):
        allure.dynamic.tag('热点为T{}的文章'.format(number % 4))
        title = self.driver.get_articles_title(number)
        self.driver.go_to_articles(number)
        assert self.driver.if_true_articles(title)

    @allure.title('Browser Cleanup热门文章链接测试')
    @pytest.mark.parametrize('number', list(range(16, 20)))
    def test_005(self, number):
        allure.dynamic.tag('热点为T{}的文章'.format(number % 4))
        title = self.driver.get_articles_title(number)
        self.driver.go_to_articles(number)
        assert self.driver.if_true_articles(title)

    @allure.title('Similar Image Finder热门文章链接测试')
    @pytest.mark.parametrize('number', list(range(20, 24)))
    def test_006(self, number):
        allure.dynamic.tag('热点为T{}的文章'.format(number % 4))
        title = self.driver.get_articles_title(number)
        self.driver.go_to_articles(number)
        assert self.driver.if_true_articles(title)

    @allure.title('Mac Uninstaller热门文章链接测试')
    @pytest.mark.parametrize('number', list(range(24, 28)))
    def test_007(self, number):
        allure.dynamic.tag('热点为T{}的文章'.format(number % 4))
        title = self.driver.get_articles_title(number)
        self.driver.go_to_articles(number)
        assert self.driver.if_true_articles(title)

    @allure.title('iMyMac PDF Compressor热门文章链接测试')
    @pytest.mark.parametrize('number', list(range(28, 32)))
    def test_008(self, number):
        allure.dynamic.tag('热点为T{}的文章'.format(number % 4))
        title = self.driver.get_articles_title(number)
        self.driver.go_to_articles(number)
        assert self.driver.if_true_articles(title)

    @allure.title('Video Converter热门文章链接测试')
    @pytest.mark.parametrize('number', list(range(32, 36)))
    def test_009(self, number):
        allure.dynamic.tag('热点为T{}的文章'.format(number % 4))
        title = self.driver.get_articles_title(number)
        self.driver.go_to_articles(number)
        assert self.driver.if_true_articles(title)

    @allure.title('Company下的链接测试')
    @pytest.mark.parametrize('key', get_branch_all_keys().get_branch_all_keys(sitemap.data, 'Company'))
    def test_010(self, key):
        allure.dynamic.tag("{}链接".format(key))
        self.driver.click_company_link(key)
        assert self.driver.if_link_is_successful(key)

    @allure.title('Products下的链接测试')
    @pytest.mark.parametrize('key', get_branch_all_keys().get_branch_all_keys(sitemap.data, 'Products'))
    def test_011(self, key):
        allure.dynamic.tag("{}链接".format(key))
        self.driver.click_products_link(key)
        assert self.driver.if_link_is_successful(key)

    @allure.title('Help下的链接测试')
    @pytest.mark.parametrize('key', get_branch_all_keys().get_branch_all_keys(sitemap.data, 'Help'))
    def test_012(self, key):
        allure.dynamic.tag("{}链接".format(key))
        self.driver.click_help_link(key)
        assert self.driver.if_link_is_successful(key)

    @allure.title('点击更多测试')
    @pytest.mark.parametrize('title', get_branch_all_keys().get_branch_all_keys(sitemap.data, 'More'))
    def test_013(self, title):
        allure.dynamic.tag("{}下的更多".format(title))
        self.driver.click_more(title)
        assert self.driver.if_articles_title(title)

    @allure.title('更多类中的文章测试')
    @pytest.mark.parametrize('key', get_branch_all_keys().get_branch_all_keys(sitemap.data, 'More')[: 9])
    def test_014(self, key):
        allure.dynamic.tag("{}下的更多中的第一篇文章".format(key))
        self.driver.click_more(key)
        self.driver.click_first_article()
        assert self.driver.if_article_succeed()
