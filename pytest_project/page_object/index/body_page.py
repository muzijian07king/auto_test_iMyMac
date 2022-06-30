import allure
from pytest_project.page.basepage import WebPage
from pytest_project.common.readelement import Element
from pytest_project.utils.times import sleep
from pytest_project.config.conf import cm

body = Element('index/body')


class BodyPage(WebPage):

    @allure.step('点击下载按钮')
    def click_ppm_download(self):
        """点击ppm下载按钮"""
        self.is_click(body.readYaml('$.download'), 1)

    @allure.step('点击详细按钮')
    def click_ppm_more(self):
        """点击ppm详细按钮"""
        self.is_click(body.readYaml('$.more'))

    def click_media(self, name):
        """点击媒体链接"""

        with allure.step(f'点击媒体{name}链接'):
            self.scroll_to_loc_is_click(body.readYaml(f'$.media.{name}'))

    def scroll_to_top(self):
        """回到顶点"""
        self.jsInDriver('document.documentElement.scrollTop=2000')
        with allure.step('点击去顶部按钮'):
            self.is_click(body['top-button'])
            sleep()

    def assert_download(self):
        self.allure_assert_or('判断是否下载成功', ('eq', cm.get_download_filename(), 'crdownload'),
                              ('eq', cm.get_download_filename(), 'pkg'))

    def assert_more(self):
        self.allure_assert('判断是否进入ppm详情页面', ('eq', self.get_current_url(), 'https://www.imymac.com/powermymac/'))

    def assert_media(self, url):
        self.allure_assert('判断是否是否进入媒体官网', ('eq', self.get_current_url(), url))

    def assert_whether_top(self):
        self.allure_assert('判断是否到达顶部', ('eq', self.getAttribute(body['top-button'], 'class'), 'top-btn t4s'),
                           ('eq', self.jsInDriver('return document.documentElement.scrollTop'), 0))
