import allure
from pytest_project.page.basepage import WebPage
from pytest_project.common.readelement import Element, get_any_key_info

foot = Element('index/foot')


class FootPage(WebPage):

    def click_link(self, link):
        """网站底部栏"""
        with allure.step('点击链接{}'.format(link)):
            self.is_click(foot[link])

    @allure.step('切换语言')
    def switch_language(self, language):
        """语言切换"""
        self.is_click(get_any_key_info(language, foot.data))

    @allure.step('点击下拉框')
    def click_drop_down_option(self):
        """点击语言切换的下拉框"""
        self.is_click(foot['Language-drop-down'])

    @allure.step('输入邮箱')
    def sendEmail(self, email):
        """输入邮箱"""
        self.input_text(foot['SearchInput'], email)

    @allure.step('点击提交按钮')
    def click_search_button(self):
        """点击提交按钮"""
        self.is_click(foot['SearchButton'])

    @allure.step('获取错误信息')
    def errorText(self):
        """获取错误信息"""
        return self.element_txet(foot['ErrorText'])

    @allure.step('获取按钮的text')
    def button_text(self):
        """获取按钮的text"""
        return self.element_txet(foot['SearchButton'])
