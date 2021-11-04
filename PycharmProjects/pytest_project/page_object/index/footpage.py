import allure
from pytest_project.page.basepage import WebPage
from pytest_project.common.readelement import Element, get_any_key_info

foot = Element('index/foot')


class FootPage(WebPage):

    def click_link(self, link):
        """网站底部栏"""
        allure.step('点击链接{}'.format(link))
        self.is_click(foot[link])

    def switch_language(self, language):
        """语言切换"""
        allure.step('切换语言')
        self.is_click(get_any_key_info(language, foot.data))

    def click_drop_down_option(self):
        """点击语言切换的下拉框"""
        allure.step('点击下拉框')
        self.is_click(foot['Language-drop-down'])

    def sendEmail(self, email):
        """输入邮箱"""
        allure.step('输入邮箱')
        self.input_text(foot['SearchInput'], email)

    def click_search_button(self):
        """点击提交按钮"""
        allure.step('点击提交按钮')
        self.is_click(foot['SearchButton'])

    def errorText(self):
        """获取错误信息"""
        allure.step('获取错误信息')
        return self.element_txet(foot['ErrorText'])

    def button_text(self):
        """获取按钮的text"""
        allure.step('获取按钮的text')
        return self.element_txet(foot['SearchButton'])
