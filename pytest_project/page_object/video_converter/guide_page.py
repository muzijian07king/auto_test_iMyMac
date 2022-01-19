from pytest_project.config.conf import cm
from pytest_project.page.basepage import WebPage
import allure
from pytest_project.common.readelement import Element, get_any_key_info

guide = Element('VideoConverter/video-guide')


class GuidePage(WebPage):

    @allure.step('下载video')
    def click_download(self):
        self.is_click(guide['free-download'])

    @allure.step('点击购买按钮')
    def goto_buy(self):
        self.is_click(guide['buy'])

    @allure.step('切换win指南')
    def cut_win_guide(self):
        self.is_click(guide['win-guide'])

    @allure.step('切换mac指南')
    def cut_mac_guide(self):
        self.is_click(guide['mac-guide'])

    @staticmethod
    def is_download():
        """判断下载是否成功"""
        return cm.get_download_filename() == 'crdownload' or cm.get_download_filename() == 'pkg' or cm. \
            get_download_filename() == 'pkg'

    def is_buy(self):
        """判断跳转购买页面内容与实际相同"""
        with allure.step('判断跳转购买页面内容与实际相同'):
            return self.find_element(guide['buy-class']) is not None

    def is_win_guide(self):
        """判断是否跳转到win指南"""
        with allure.step('判断是否跳转到win指南'):
            return self.element_text(guide['guide-header']) == "How to Use iMyMac Video Converter on Windows"

    def is_mac_guide(self):
        """判断是否跳转到mac指南"""
        with allure.step('判断是否跳转到mac指南'):
            return self.element_text(guide['guide-header']) == "How to Use iMyMac Video Converter on Mac"

    @allure.step('点击文章链接')
    def click_article(self, article_name):
        self.is_click(get_any_key_info(article_name, guide.data))

    @allure.step('移动到文章栏上')
    def scroll_to_article(self):
        self.scroll_to_loc(guide['article-class'])

    def is_article(self, article_name):
        with allure.step('判断是否跳转到文章'):
            return article_name.replace('-', ' ') in self.element_text(guide['article-handle']).lower()
