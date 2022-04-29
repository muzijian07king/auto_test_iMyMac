import allure
from pytest_project.page.basepage import WebPage
from pytest_project.common.readelement import Element

head = Element('index/head')


class HeadPage(WebPage):
    """网站头部导航栏"""

    @allure.step('进入首页')
    def click_index_loge(self):
        """点击loge按钮"""
        self.is_click(head['index'])

    @allure.step('移动到Product&Solution下拉框')
    def move_product_solution_dropdown(self):
        """下拉框点击元素"""
        self.move_element(head['Product&Solution'])

    def click_utility(self, utility):
        """进入应用程序页面"""
        with allure.step('进入{}页面'.format(utility)):
            self.is_click(head.readYaml(f'$.Utility.{utility}'))

    def click_online(self, online):
        """进入应用程序页面"""
        with allure.step('进入{}在线工具页面'.format(online)):
            self.is_click(head.readYaml(f'$.Online.{online}'))

    @allure.step('进入商店')
    def click_store(self):
        """点击Store按钮"""
        self.is_click(head['Store'])

    @allure.step('进入帮助页面')
    def click_support(self):
        """点击Support按钮"""
        self.is_click(head['Support'])

    @allure.step('点击搜索按钮')
    def click_search(self):
        """点击搜索按钮"""
        self.is_click(head['search'])

    @allure.step('关闭搜索输入框')
    def close_search(self):
        """点击关闭按钮"""
        self.is_click(head['search-close'])

    @allure.step('输入关键字')
    def send_search(self, text):
        """搜索框输入关键字"""
        self.input_text(head['search-input'], text)

    @allure.step('按下回车')
    def search_enter(self):
        """按下回车"""
        self.Key_enter(head['search-input'])

    def assert_index(self):
        """判断是否回到首页"""
        self.allure_assert('判断是否回到首页', ('eq', self.get_current_url(), 'https://www.imymac.com/index.html'))

    def assert_utility(self, utility: str):
        """判断是否进入到应用页面"""
        self.allure_assert(f"判断是否进入到{utility}页面",
                           ('eq', self.get_current_url(), f'https://www.imymac.com/{utility.lower()}/'))

    def assert_online(self, utility: str):
        """判断是否进入到在线体验应用页面"""
        self.allure_assert(f"判断是否进入到{utility}在线工具页面", (
            'eq', self.get_current_url(), f'https://www.imymac.com/{utility.replace("Free", "online").lower()}/'))

    def assert_store(self):
        """判断是否进入商店页面"""
        self.allure_assert('判断是否进入商店页面', ('eq', self.get_current_url(), 'https://www.imymac.com/store/'))

    def assert_support(self):
        """判断是否进入商店页面"""
        self.allure_assert('判断是否进入客服支援页面', ('eq', self.get_current_url(), 'https://www.imymac.com/support/'))

    def assert_search(self, text):
        """判断是否根据关键字搜索"""
        self.allure_assert('判断是否根据关键字搜索', (
            'eq', self.get_current_url(), f'https://www.imymac.com/resource/?q={text}'.replace(' ', '+')))

    def assert_close_search(self):
        """判断是否取消搜索"""
        self.allure_assert('判断是否取消搜索', ('eq', self.is_display(head.readYaml('$.search-input')), False))
