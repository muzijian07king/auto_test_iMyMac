import allure
from pytest_project.page.basepage import WebPage
from pytest_project.common.readelement import Element, get_any_key_info

foot = Element('index/foot')
lge = Element('index/language')


class FootPage(WebPage):

    def click_link(self, link):
        """网站底部栏"""
        with allure.step('点击底部超链接{}'.format(link)):
            self.is_click(get_any_key_info(link, foot.data))

    @allure.step('点击语言下拉框')
    def click_drop_down_option(self):
        """点击下拉框"""
        self.is_click(foot.readYaml('$.Language-drop-down'))

    @allure.step('切换语言')
    def switch_language(self, language):
        """语言切换"""
        self.is_click(foot.readYaml(f'$.Language.{language}'))

    def input_email(self, email):
        """输入邮箱"""
        with allure.step('输入邮箱：{}'.format(email)):
            self.input_text(foot.readYaml('$.InputEmail'), email)

    @allure.step('点击提交按钮')
    def click_submit(self):
        """点击提交按钮"""
        self.is_click(foot['SearchButton'], 1)

    def scroll_copyright(self):
        self.jsInDriver('document.documentElement.scrollTop=10000')

    @allure.step('点击授权cookie隐私')
    def click_ok_use_cookie(self):
        self.is_click(foot['ok'])

    def click_privacy_link(self):
        self.is_click(foot['privacy'])

    def assert_use_cookie(self):
        self.allure_assert('判断是否使用cookie', ('eq', self.getAttribute(foot['box-cookies'], 'class'), 'box-cookies'))

    def assert_goto_privacy(self):
        self.allure_assert('判断是否跳转隐私页面', ('eq', self.get_current_url(), 'https://www.imymac.com/privacy.html'))

    def assert_link(self, url):
        self.allure_assert('判断是否跳转链接', ('eq', self.get_current_url(), url))

    def assert_switch_language(self, language, url):
        self.allure_assert(f'判断语言是否切换为{lge.getLanguage(language)}', ('eq', self.get_current_url(), url))

    def assert_submit_email(self):
        self.allure_assert('判断提交邮箱成功', ('eq', self.getAttribute(foot['success'], 'class'), 'box-thanks display'))

    def assert_fail_submit_email(self):
        self.allure_assert('判断提交邮箱失败',
                           ('eq', self.element_text(foot['ErrorText']), 'Please enter a valid email address.'))

    def assert_copyright(self):
        self.allure_assert('判断著作权是否正确', (
            'eq', self.element_text(foot['copyright']), 'Copyright © 2022 iMyMac. All rights reserved.'))
