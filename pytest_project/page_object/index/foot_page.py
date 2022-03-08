import allure
from pytest_project.page.basepage import WebPage
from pytest_project.common.readelement import Element, get_any_key_info
from pytest_project.utils.logger import log

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
        self.is_click(foot['SearchButton'])

    def errorText(self):
        """获取错误信息"""
        return self.element_text(foot['ErrorText'])

    def success_submit(self):
        return self.getAttribute(foot['success'], 'class') == 'box-thanks display'

    def scroll_copyright(self):
        self.jsInDriver('document.documentElement.scrollTop=10000')

    @allure.step('点击授权cookie隐私')
    def click_ok_use_cookie(self):
        self.is_click(foot['ok'])

    def click_privacy_link(self):
        self.is_click(foot['privacy'])

    def assert_use_cookie(self):
        result = self.getAttribute(foot['box-cookies'], 'class') == 'box-cookies'
        self.allure_assert_step("判断是否使用cookie", result)
        assert result

    def assert_goto_privacy(self):
        result = self.get_current_url() == 'https://www.imymac.com/privacy.html'
        self.allure_assert_step("判断是否跳转隐私页面", result)
        assert result

    def assert_link(self, url):
        result = self.get_current_url() == url
        self.allure_assert_step("判断是否跳转链接", result)
        assert result

    def assert_switch_language(self, language, url):
        result = self.get_current_url() == url
        self.allure_assert_step(f'判断语言是否切换为{lge.getLanguage(language)}', result)
        assert result

    def assert_submit_email(self):
        result = self.success_submit()
        self.allure_assert_step('判断提交邮箱成功', result)
        assert result

    def assert_fail_submit_email(self):
        result = self.errorText() == 'Please enter a valid email address.'
        self.allure_assert_step('判断提交邮箱失败', result)
        assert result

    def assert_copyright(self):
        result = self.element_text(foot['copyright']) == \
                 'Copyright © 2022 iMyMac. All rights reserved.'
        self.allure_assert_step('判断著作权是否正确', result)
        assert result
