import allure

from pytest_project.page.basepage import WebPage
from pytest_project.common.readelement import Element, get_any_key_info

about = Element('SiteMap/about')


class AboutPage(WebPage):
    def click_product_link(self, product):
        allure.step('点击产品<{}>链接'.format(product))
        self.is_click(get_any_key_info(product, about.data))

    def if_product_link(self, product):
        with allure.step('判断产品链接是否正确'):
            return product in self.element_txet(about['h1'])
