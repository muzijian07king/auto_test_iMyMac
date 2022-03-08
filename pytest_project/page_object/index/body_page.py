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
        self.is_click(body.readYaml('$.download'))

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
        result = cm.get_download_filename() == 'crdownload' or \
                 cm.get_download_filename() == 'pkg'
        self.allure_assert_step('判断是否下载成功', result)
        assert result

    def assert_more(self):
        result = self.get_current_url() == 'https://www.imymac.com/powermymac/'
        self.allure_assert_step('判断是否进入ppm详情页面', result)
        assert result

    def assert_media(self, url):
        result = self.get_current_url() == url
        self.allure_assert_step('判断是否是否进入媒体官网', result)
        assert result

    def assert_whether_top(self):
        result = self.getAttribute(body['top-button'], 'class') == 'top-btn t4s' and \
                   self.jsInDriver('return document.documentElement.scrollTop') == 0
        self.allure_assert_step('判断是否到达顶部', result)
        assert result
