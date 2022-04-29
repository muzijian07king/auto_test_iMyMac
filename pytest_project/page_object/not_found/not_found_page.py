from pytest_project.page.basepage import WebPage
from pytest_project.common.readelement import Element
import allure

NotFound = Element('404/404')


class NotFoundPage(WebPage):
    @allure.step('点击去首页')
    def goto_home(self):
        self.is_click(NotFound['home'])

    @allure.step('点击去帮助页面')
    def goto_support(self):
        self.is_click(NotFound['support'])

    @allure.step('点击去购买页面')
    def goto_store(self):
        self.is_click(NotFound['store'])

    @allure.step('点击去博客')
    def goto_blog(self):
        self.is_click(NotFound['blog'])

    def assert_goto_home(self):
        self.allure_assert("判断是否跳转首页", ('eq', self.get_current_url(), 'https://www.imymac.com/index.html'))

    def assert_goto_support(self):
        self.allure_assert('判断是否跳转帮助页面', ('eq', self.get_current_url(), 'https://www.imymac.com/support/'))

    def assert_goto_store(self):
        self.allure_assert('判断是否跳转购买页面', ('eq', self.get_current_url(), 'https://www.imymac.com/store/'))

    def assert_goto_blog(self):
        self.allure_assert('判断是否跳转博客页面', ('eq', self.get_current_url(), 'https://www.imymac.com/resource/'))
