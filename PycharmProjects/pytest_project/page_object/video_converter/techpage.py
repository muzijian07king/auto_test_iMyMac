from pytest_project.config.conf import cm
from pytest_project.page.basepage import WebPage
import allure
from pytest_project.common.readelement import Element, get_any_key_info

tech = Element('VideoConverter/video-tech')


class TechPage(WebPage):

    @allure.step('下载video')
    def click_download(self):
        self.is_click(tech['free-download'])

    @allure.step('点击购买按钮')
    def goto_buy(self):
        self.is_click(tech['buy'])

    @allure.step('进入tech页面')
    def goto_index(self):
        self.is_click(tech['index'])

    @allure.step('下载进入技巧界面')
    def goto_guide(self):
        self.is_click(tech['guide'])

    @staticmethod
    def is_download():
        """判断下载是否成功"""
        return cm.get_download_filename() == 'crdownload' or cm.get_download_filename() == 'pkg'

    def is_buy(self):
        """判断跳转购买页面内容与实际相同"""
        return self.find_element(tech['buy-class']) is not None

    def is_index(self):
        """判断是否跳转到主页"""
        return self.find_element(tech['support-body']) is not None and self.element_txet(tech['support-handle']) == \
               "Supported Elements for Video Converter"

    def is_guide(self):
        return self.element_txet(tech['guide-handle']) == 'How to Use iMyMac Video Converter'

    @allure.step('点击文章链接')
    def click_article(self, article_name):
        self.is_click(get_any_key_info(article_name, tech.data))

    @allure.step('移动到文章栏上')
    def scroll_to_article(self):
        self.scroll_to_loc(tech['article-class'])

    def is_article(self, article_name):
        return article_name.replace('-', ' ') in self.element_txet(tech['article-handle']).lower()
