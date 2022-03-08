import allure
import pytest

from pytest_project.page_object.sitemap.sitemap_page import SitemapPage
from pytest_project.common.readconfig import ini
from pytest_project.common.readexcel import getExcelAllData


@allure.feature('网址地图页面测试')
@allure.story('跳转功能测试')
class TestBody(object):
    @pytest.fixture(scope='function', autouse=True)
    def open_url(self, drivers):
        self.driver = SitemapPage(drivers)
        self.driver.get_url(ini.get_url('sitemap'))

    @allure.title('跳转企业介绍页面测试')
    @pytest.mark.parametrize('name,url', getExcelAllData('company', 'SiteMap/sitemap.xlsx'))
    def test_001(self, name, url):
        allure.dynamic.tag(name)
        self.driver.goto_company_webpage(name)
        self.driver.assert_goto_webpage_succeed(url)

    @allure.title('跳转产品介绍页面测试')
    @pytest.mark.parametrize('name,url', getExcelAllData('products', 'SiteMap/sitemap.xlsx'))
    def test_002(self, name, url):
        allure.dynamic.tag(name)
        self.driver.goto_products_webpage(name)
        self.driver.assert_goto_webpage_succeed(url)

    @allure.title('跳转帮助页面测试')
    @pytest.mark.parametrize('name,url', getExcelAllData('help', 'SiteMap/sitemap.xlsx'))
    def test_003(self, name, url):
        allure.dynamic.tag(name)
        self.driver.goto_help_webpage(name)
        self.driver.assert_goto_webpage_succeed(url)
