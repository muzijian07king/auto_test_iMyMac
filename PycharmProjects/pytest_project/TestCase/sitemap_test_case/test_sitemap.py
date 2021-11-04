import allure
import pytest

from pytest_project.page_object.sitemap.sitemap_page import SitemapPage
from pytest_project.common.readconfig import ini


class TestBody(object):
    @pytest.fixture(scope='function', autouse=True)
    def open_url(self, drivers):
        self.driver = SitemapPage(drivers)
        self.driver.get_url(ini.get_url('sitemap'))

    @allure.title('热门文章链接测试')
    @pytest.mark.parametrize('number', list(range(36)))
    def test_001(self, number):
        allure.dynamic.tag('热点为T{}的文章'.format(number % 4))
        title = self.driver.get_articles_title(number)
        self.driver.go_to_articles(number)
        assert self.driver.if_true_articles(title)
