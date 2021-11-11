import allure
import pytest

from pytest_project.page_object.sitemap.about_page import AboutPage
from pytest_project.common.readconfig import ini
from pytest_project.common.readelement import Element, get_branch_all_keys

about = Element('SiteMap/about')


@allure.feature('网址地图页面测试')
@allure.story('关于我们功能测试')
class TestBody(object):
    @pytest.fixture(scope='function', autouse=True)
    def open_url(self, drivers):
        self.driver = AboutPage(drivers)
        self.driver.get_url(ini.get_url('about'))

    @allure.title('产品链接测试')
    @pytest.mark.parametrize('product', get_branch_all_keys().get_branch_all_keys(about.data, 'about'))
    def test_001(self, product):
        allure.tag('产品<{}>链接'.format(product))
        self.driver.click_product_link(product)
        assert self.driver.if_product_link(product)