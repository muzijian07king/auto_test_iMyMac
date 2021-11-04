import allure
from pytest_project.page.basepage import WebPage
from pytest_project.common.readelement import Element

head = Element('index/head')


class HeadPage(WebPage):
    """网站头部导航栏"""

    @allure.step('点击PowerMyMac下拉框')
    def move_PowerMyMac_dropdown(self):
        """下拉框点击元素"""
        self.move_element(head['PowerMyMac'])

    @allure.step('点击OnlineTools下拉框')
    def move_OnlineTools_dropdown(self):
        self.move_element(head['Online-Tools'])

    def click_link(self, link):
        """点击超链接"""
        allure.step('点击{}超链接'.format(link))
        self.is_click(head[link])

    @allure.step('点击搜索按钮')
    def click_search(self):
        """点击搜索按钮"""
        self.is_click(head['search'])

    @allure.step('输入关键字')
    def send_search(self, text):
        """搜索框输入关键字"""
        self.input_text(head['search-input'], text)

    @allure.step('按下回车')
    def search_enter(self):
        """按下回车"""
        self.Key_enter(head['search-input'])

