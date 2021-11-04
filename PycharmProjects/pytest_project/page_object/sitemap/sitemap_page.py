import allure

from pytest_project.page.basepage import WebPage
from pytest_project.common.readelement import Element

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
            return self.element_txet(sitemap['articles-title']) == title or (
                        len(title.split(' ')) + len(self.element_txet(sitemap['articles-title']))) - \
                   set(title.split(' ') + self.element_txet(sitemap['articles-title'])) >= 2
