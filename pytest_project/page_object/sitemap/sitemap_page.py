import allure

from pytest_project.page.basepage import WebPage
from pytest_project.common.readelement import Element, get_branch_value_with_key

sitemap = Element('SiteMap/siteMap')


class SitemapPage(WebPage):
    @allure.step('点击文章链接')
    def go_to_articles(self, number):
        elements = self.find_elements(sitemap['articles-links'])
        elements[number].click()

    def get_articles_title(self, number):
        elements = self.find_elements(sitemap['articles-links'])
        return elements[number].text

    def if_true_articles(self, title):
        with allure.step('获取文章标题==》{}'.format(title)):
            return self.element_text(sitemap['articles-title']) == title or (
                        len(title.split(' ')) + len(self.element_text(sitemap['articles-title']))) - \
                   len(set(title.split(' ') + self.element_text(sitemap['articles-title']).split(' '))) >= 2

    @allure.step('点击Company下的链接')
    def click_company_link(self, key):
        self.is_click(get_branch_value_with_key(key, sitemap.data, 'Company'))

    @allure.step('点击Products下的链接')
    def click_products_link(self, key):
        self.is_click(get_branch_value_with_key(key, sitemap.data, 'Products'))

    @allure.step('点击Help下的链接')
    def click_help_link(self, key):
        self.is_click(get_branch_value_with_key(key, sitemap.data, 'Help'))

    def if_link_is_successful(self, key):
        with allure.step('判断链接是否成功'):
            return key.lower() in self.get_diver_title().lower()

    def click_more(self, key):
        with allure.step('点击{}栏下的更多按钮'.format(key)):
            self.is_click(get_branch_value_with_key(key, sitemap.data, 'More'))

    def if_articles_title(self, key):
        with allure.step('判断更多按钮是否跳转'):
            return key == self.element_text(sitemap['articles-class'])

    @allure.step('点击第一篇文章')
    def click_first_article(self):
        self.is_click(sitemap['articles-link'])

    def if_article_succeed(self):
        with allure.step('判断跳转是否成功'):
            return '404' not in self.get_diver_title()
