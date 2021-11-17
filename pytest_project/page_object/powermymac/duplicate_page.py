import logging

import allure

from pytest_project.page.basepage import WebPage
from pytest_project.common.readelement import Element
from pytest_project.config.conf import cm
from pytest_project.utils.times import sleep

duplicate = Element('PowerMyMac/common')


class DuplicatePage(WebPage):
    @allure.step('点击下载链接')
    def download_mac_cleaner(self, loc):
        """点击下载按钮"""
        self.is_click(loc)

    @allure.step('去购买页面')
    def goto_buy(self, loc):
        """去购买页面"""
        self.is_click(loc)

    @allure.step('点击超链接')
    def click_link(self, link):
        """点击链接"""
        self.is_click(link)

    @allure.step('切换轮播图')
    def click_carousel(self):
        """点击评论轮播图下的索引按钮"""
        self.is_click(duplicate['carousel-li'])

    def return_carousel_index(self):
        """获取当前评论轮播图的索引"""
        with allure.step('判断评论轮播图是否切换成功'):
            return self.getAttribute(duplicate['carousel-inner'], 'class') == 'item active'

    def is_menu(self):
        """判断滑动到中间位置后menu是否出现"""
        with allure.step('判断滑动到中间位置后menu是否出现'):
            return self.getAttribute(duplicate['fix-menu'], 'class') == 'fixMenu fixIt'

    def is_goto_buy(self):
        """判断跳转购买页面内容与实际相同"""
        with allure.step("判断跳转购买页面内容与实际相同"):
            return self.find_element(duplicate['buy-month']) is not None

    def is_goto_guide(self):
        """判断跳转手册页面内容与实际相同"""
        with allure.step('判断跳转手册页面内容与实际相同'):
            return self.element_txet(duplicate['guide-handline']) == 'PowerMyMac User Guide'

    def is_cleaner_index(self):
        """判断跳转首页页面内容与实际相同"""
        with allure.step('判断跳转首页页面内容与实际相同'):
            return self.element_txet(duplicate['cleaner-handline']) == 'PowerMyMac - Duplicate Finder'

    def scroll_to_menu(self):
        """移动到menu栏"""
        allure.step('页面滑动到menu上')
        self.scroll_to_loc(duplicate['menu-css'])

    @allure.step('页面滑动到footerBg上')
    def scroll_to_footerBg(self):
        """移动到footerBg栏"""
        self.scroll_to_loc(duplicate['footerBg-class'])

    @allure.step('页面滑动到borderBG2上')
    def scroll_to_borderBG2(self):
        """移动到borderBG2栏"""
        self.scroll_to_loc(duplicate['borderBG2-class'])

    @allure.step('页面滑动到container_text上')
    def scroll_to_container_text(self):
        """移动到container_text栏"""
        self.scroll_to_loc(duplicate['container-text-center-class'])

    @allure.step('页面滑动到carousel_comment上')
    def scroll_to_carousel_comment(self):
        """移动到carousel_comment栏"""
        self.scroll_to_loc(duplicate['carousel-comment-class'])

    @staticmethod
    def is_download():
        """判断下载是否成功"""
        return cm.get_download_filename() == 'crdownload' or cm.get_download_filename() == 'pkg'

    @allure.step('进入文章页面')
    def click_article_link(self, link):
        """点击文章链接"""
        self.is_click(duplicate[link])

    def is_goto_article(self, link):
        """判断是否到达文章页面"""
        with allure.step('判断是否到达文章页面'):
            return self.find_element(duplicate['article-body']) is not None and link in self.get_current_url()

    @allure.step('切换The Andvantage of Browser Cleanup轮播图')
    def click_carousel_indicators(self):
        """The Andvantage of Browser Cleanup轮播图的切换"""
        self.is_click(duplicate['carousel-indicators-li'])

    def return_carousel_indicators_index(self):
        """获取当前The Andvantage of Browser Cleanup轮播图的索引"""
        with allure.step('判断轮播图是否切换成功'):
            return self.getAttribute(duplicate['carousel-indicators-inner'], 'class') == 'item active'
