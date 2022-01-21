from pytest_project.page.basepage import WebPage
from pytest_project.common.readelement import Element, get_any_key_info
import allure

buy = Element('Store/buy-option')


class BuyPage(WebPage):

    @allure.step('单击购买套餐1按钮')
    def click_buy_1_button(self):
        self.is_click(get_any_key_info('one License', buy.data))

    @allure.step('单击购买套餐2按钮')
    def click_buy_2_button(self):
        self.is_click(get_any_key_info('two License', buy.data))

    @allure.step('单击购买套餐3按钮')
    def click_buy_3_button(self):
        self.is_click(get_any_key_info('three License', buy.data))

    def is_goto_buy(self):
        """判断是否弹出支付弹窗"""
        with allure.step('判断是否弹出支付弹窗'):
            return self.find_element(buy['iframe']) is not None

    def return_price_in_license(self):
        """返回每个套餐标题以及价格，以元组形式储存各自数据，然后总体以数组形式，便于参数化"""
        return list(map(lambda x, y: (x, y), self.elements_text(buy['licenseTime']),
                        self.elements_text(buy['licensePrice'])))

    @allure.step('点击pmm的更多选项按钮')
    def goto_pmm_option(self):
        self.is_click(buy['pmm-option'])

    @allure.step('点击video的更多选项按钮')
    def goto_video_option(self):
        self.is_click(buy['video-option'])

    @allure.step('切换购买家庭永久套餐按钮')
    def click_pmm_lifetime_license_family(self):
        self.is_click(buy['pmm-family-license'])

    @allure.step('切换购买个人永久套餐按钮')
    def click_pmm_lifetime_license_single(self):
        self.is_click(buy['pmm-family-license'])
        self.is_click(buy['pmm-single-license'])

    @allure.step('切换win端video converter购买页面')
    def cut_win_video_converter(self):
        self.is_click(buy['video-win-buy'])

    @allure.step('切换mac端video converter购买页面')
    def cut_mac_video_converter(self):
        self.is_click(buy['video-mac-buy'])

    def is_cut_win_buy_video_converter(self):
        """判断是否切换win端购买video-converter页面"""
        with allure.step('判断是否切换win端购买video-converter页面'):
            return 'win' in self.getAttribute(buy['system-ui'], 'class') and \
                    'active' in self.getAttribute(buy['video-win-buy'], 'class')

    def is_cut_mac_buy_video_converter(self):
        """判断是否切换mac端购买video-converter页面"""
        with allure.step('判断是否切换mac端购买video-converter页面'):
            return 'apple' in self.getAttribute(buy['system-ui'], 'class') and \
                    'active' in self.getAttribute(buy['video-mac-buy'], 'class')

    def is_buy_family(self):
        """判断是否切换购买家庭永久套餐成功"""
        with allure.step('判断是否切换购买家庭永久套餐成功'):
            return self.getAttribute(buy['selectButton'], 'class') == 'selectButton chosenRight' and \
                   '49.95' in self.elements_text(buy['licensePrice'])

    def is_buy_single(self):
        """判断是否切换购买个人永久套餐成功"""
        with allure.step('判断是否切换购买个人永久套餐成功'):
            return self.getAttribute(buy['selectButton'], 'class') == 'selectButton' and \
                   '29.95' in self.elements_text(buy['licensePrice'])
