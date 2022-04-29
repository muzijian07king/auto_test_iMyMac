from pytest_project.page.basepage import WebPage
from pytest_project.common.readelement import Element
import allure

profile = Element('Profile/profile')


class ProfilePage(WebPage):

    def close_cookie_popup(self):
        self.jsInDriver("document.querySelector('div.box-cookies').className = 'box-cookies'")

    @allure.step('进入左侧作者详情页面')
    def goto_left_writer(self):
        name = self.element_text(profile['left-writer-name'])
        self.is_click(profile['left-writer-more'])
        return name

    @allure.step('进入中间作者详情页面')
    def goto_mid_writer(self):
        name = self.element_text(profile['mid-writer-name'])
        self.is_click(profile['mid-writer-more'])
        return name

    @allure.step('进入右侧作者详情页面')
    def goto_right_writer(self):
        name = self.element_text(profile['right-writer-name'])
        self.is_click(profile['right-writer-more'])
        return name

    def assert_goto_writer(self, name):
        self.allure_assert('判断跳转到作者更多作品页面', ('eq', self.element_text(profile['name']), name))

    @allure.step('点击第一篇文章')
    def click_articles(self):
        self.close_cookie_popup()
        title = self.element_text(profile['popular-articles'])
        self.click_elements(profile['popular-articles'])
        return title

    def assert_goto_articles(self, title):
        self.allure_assert('判断是否跳转文章', ('eq', self.element_text(profile['h1']), title))

    @allure.step('点击第一篇科学技术')
    def click_tech(self):
        self.close_cookie_popup()
        self.click_elements(profile['tech-hut'])

    @allure.step('点击查看更多more科学技术')
    def click_more(self):
        self.close_cookie_popup()
        self.click_elements(profile['tech-more'])

    def assert_goto_tech(self):
        self.allure_assert('判断是否跳转科学文章', ('not_eq', self.element_text(profile['h1']), None))

