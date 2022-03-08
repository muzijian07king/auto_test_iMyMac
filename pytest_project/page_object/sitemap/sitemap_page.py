import allure

from pytest_project.page.basepage import WebPage
from pytest_project.common.readelement import Element, get_branch_value_with_key

sitemap = Element('SiteMap/siteMap')


class SitemapPage(WebPage):

    @allure.step('跳转到公司介绍页面')
    def goto_company_webpage(self, name):
        self.is_click(sitemap.readYaml(f'$.Company.{name}'))

    @allure.step('跳转到公司产品页面')
    def goto_products_webpage(self, name):
        self.is_click(sitemap.readYaml(f'$.Products.{name}'))

    @allure.step('跳转到帮助页面')
    def goto_help_webpage(self, name):
        self.is_click(sitemap.readYaml(f'$.Help.{name}'))

    def assert_goto_webpage_succeed(self, url):
        result = self.get_current_url() == url
        self.allure_assert_step(f'判断成功跳转：{url},', result)
        assert result
