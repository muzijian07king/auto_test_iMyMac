import allure

from pytest_project.page.basepage import WebPage
from pytest_project.common.readelement import Element
from pytest_project.common.readexcel import getValueByIndex

store = Element('Store/video-store-option')


class OptionPage(WebPage):
    def assert_mac_month_original_price(self):
        self.allure_assert('判断产品购买一个月原价', ('eq', self.element_text(store.readYaml('$.month.original-price')),
                                           getValueByIndex(2, 2, 'video-mac套餐价格', 'Store/store.xlsx')))

    def assert_mac_month_now_price(self):
        self.allure_assert('判断产品购买一个月现价', ('eq', self.element_text(store.readYaml('$.month.now-price')),
                                           getValueByIndex(3, 2, 'video-mac套餐价格', 'Store/store.xlsx')))

    def assert_mac_month_discounts_price(self):
        self.allure_assert('判断产品购买一个月优惠价', ('eq', self.element_text(store.readYaml('$.month.discounts-price')),
                                            getValueByIndex(4, 2, 'video-mac套餐价格', 'Store/store.xlsx')))

    def assert_mac_year_original_price(self):
        self.allure_assert('判断产品购买一个年原价', ('eq', self.element_text(store.readYaml('$.year.original-price')),
                                           getValueByIndex(2, 3, 'video-mac套餐价格', 'Store/store.xlsx')))

    def assert_mac_year_now_price(self):
        self.allure_assert('判断产品购买一个年现价', ('eq', self.element_text(store.readYaml('$.year.now-price')),
                                           getValueByIndex(3, 3, 'video-mac套餐价格', 'Store/store.xlsx')))

    def assert_mac_year_discounts_price(self):
        self.allure_assert('判断产品购买一个年优惠价', ('eq', self.element_text(store.readYaml('$.year.discounts-price')),
                                            getValueByIndex(4, 3, 'video-mac套餐价格', 'Store/store.xlsx')))

    def assert_mac_lifetime_one_original_price(self):
        self.allure_assert('判断产品购买永久一个设备原价',
                           ('eq', self.element_text(store.readYaml('$.lifetime-license.one.original-price')),
                            getValueByIndex(2, 4, 'video-mac套餐价格', 'Store/store.xlsx')))

    def assert_mac_lifetime_one_now_price(self):
        self.allure_assert('判断产品购买永久一个设备现价',
                           ('eq', self.element_text(store.readYaml('$.lifetime-license.one.now-price')),
                            getValueByIndex(3, 4, 'video-mac套餐价格', 'Store/store.xlsx')))

    def assert_mac_lifetime_one_discounts_price(self):
        self.allure_assert('判断产品购买永久一个设备优惠价',
                           ('eq', self.element_text(store.readYaml('$.lifetime-license.one.discounts-price')),
                            getValueByIndex(4, 4, 'video-mac套餐价格', 'Store/store.xlsx')))

    def assert_mac_lifetime_five_original_price(self):
        self.allure_assert('判断产品购买永久五个设备原价',
                           ('eq', self.element_text(store.readYaml('$.lifetime-license.five.original-price')),
                            getValueByIndex(2, 5, 'video-mac套餐价格', 'Store/store.xlsx')))

    def assert_mac_lifetime_five_now_price(self):
        self.allure_assert('判断产品购买永久五个设备现价',
                           ('eq', self.element_text(store.readYaml('$.lifetime-license.five.now-price')),
                            getValueByIndex(3, 5, 'video-mac套餐价格', 'Store/store.xlsx')))

    def assert_mac_lifetime_five_discounts_price(self):
        self.allure_assert('判断产品购买永久五个设备优惠价',
                           ('eq', self.element_text(store.readYaml('$.lifetime-license.five.discounts-price')),
                            getValueByIndex(4, 5, 'video-mac套餐价格', 'Store/store.xlsx')))

    def assert_win_month_original_price(self):
        self.allure_assert('判断产品购买一个月原价', ('eq', self.element_text(store.readYaml('$.month.original-price')),
                                           getValueByIndex(2, 2, 'video-win套餐价格', 'Store/store.xlsx')))

    def assert_win_month_now_price(self):
        self.allure_assert('判断产品购买一个月现价', ('eq', self.element_text(store.readYaml('$.month.now-price')),
                                           getValueByIndex(3, 2, 'video-win套餐价格', 'Store/store.xlsx')))

    def assert_win_month_discounts_price(self):
        self.allure_assert('判断产品购买一个月优惠价', ('eq', self.element_text(store.readYaml('$.month.discounts-price')),
                                            getValueByIndex(4, 2, 'video-win套餐价格', 'Store/store.xlsx')))

    def assert_win_year_original_price(self):
        self.allure_assert('判断产品购买一个年原价', ('eq', self.element_text(store.readYaml('$.year.original-price')),
                                           getValueByIndex(2, 3, 'video-win套餐价格', 'Store/store.xlsx')))

    def assert_win_year_now_price(self):
        self.allure_assert('判断产品购买一个年现价', ('eq', self.element_text(store.readYaml('$.year.now-price')),
                                           getValueByIndex(3, 3, 'video-win套餐价格', 'Store/store.xlsx')))

    def assert_win_year_discounts_price(self):
        self.allure_assert('判断产品购买一个年优惠价', ('eq', self.element_text(store.readYaml('$.year.discounts-price')),
                                            getValueByIndex(4, 3, 'video-win套餐价格', 'Store/store.xlsx')))

    def assert_win_lifetime_one_original_price(self):
        self.allure_assert('判断产品购买永久一个设备原价',
                           ('eq', self.element_text(store.readYaml('$.lifetime-license.one.original-price')),
                            getValueByIndex(2, 4, 'video-win套餐价格', 'Store/store.xlsx')))

    def assert_win_lifetime_one_now_price(self):
        self.allure_assert('判断产品购买永久一个设备现价',
                           ('eq', self.element_text(store.readYaml('$.lifetime-license.one.now-price')),
                            getValueByIndex(3, 4, 'video-win套餐价格', 'Store/store.xlsx')))

    def assert_win_lifetime_one_discounts_price(self):
        self.allure_assert('判断产品购买永久一个设备优惠价',
                           ('eq', self.element_text(store.readYaml('$.lifetime-license.one.discounts-price')),
                            getValueByIndex(4, 4, 'video-win套餐价格', 'Store/store.xlsx')))

    def assert_win_lifetime_five_original_price(self):
        self.allure_assert('判断产品购买永久五个设备原价',
                           ('eq', self.element_text(store.readYaml('$.lifetime-license.five.original-price')),
                            getValueByIndex(2, 5, 'video-win套餐价格', 'Store/store.xlsx')))

    def assert_win_lifetime_five_now_price(self):
        self.allure_assert('判断产品购买永久五个设备现价',
                           ('eq', self.element_text(store.readYaml('$.lifetime-license.five.now-price')),
                            getValueByIndex(3, 5, 'video-win套餐价格', 'Store/store.xlsx')))

    def assert_win_lifetime_five_discounts_price(self):
        self.allure_assert('判断产品购买永久五个设备优惠价',
                           ('eq', self.element_text(store.readYaml('$.lifetime-license.five.discounts-price')),
                            getValueByIndex(4, 5, 'video-win套餐价格', 'Store/store.xlsx')))

    @allure.step('切换到win版')
    def switch_win(self):
        self.is_click(store['mac'])
        self.is_click(store['win'])

    @allure.step('切换到mac版')
    def switch_mac(self):
        self.is_click(store['mac'])

    def assert_switch_win(self):
        self.allure_assert('判断切换win是否成功', ('eq', self.getAttribute(store['win'], 'class'), 'version-win active'))

    def assert_switch_mac(self):
        self.allure_assert('判断切换mac是否成功', ('eq', self.getAttribute(store['mac'], 'class'), 'version-mac active'))

    @allure.step("点击购买一个月套餐按钮")
    def click_buy_month_button(self):
        self.is_click(store.readYaml('$.month.buy'))

    @allure.step("点击购买一个年套餐按钮")
    def click_buy_year_button(self):
        self.is_click(store.readYaml('$.year.buy'))

    @allure.step("切换到永久一台套餐")
    def switch_to_lifetime_one_button(self):
        self.is_click(store.readYaml("$.lifetime-license.one.option"))

    @allure.step("切换到永久五台套餐")
    def switch_to_lifetime_five_button(self):
        self.is_click(store.readYaml("$.lifetime-license.five.option"))

    @allure.step("点击购买永久一台套餐按钮")
    def click_buy_lifetime_one_button(self):
        self.scroll_to_loc_is_click(store.readYaml('$.lifetime-license.one.buy'))

    @allure.step("点击购买永久五台套餐按钮")
    def click_buy_lifetime_five_button(self):
        self.scroll_to_loc_is_click(store.readYaml('$.lifetime-license.five.buy'))

    @allure.step('切换到win购买一个月套餐弹窗')
    def switch_to_win_month_pay(self):
        self.switch_to_frame(store.readYaml('$.month.iframe.win', 1))

    @allure.step('切换到mac购买一个月套餐弹窗')
    def switch_to_mac_month_pay(self):
        self.switch_to_frame(store.readYaml('$.month.iframe.mac', 1))

    @allure.step('切换到win购买一年套餐弹窗')
    def switch_to_win_year_pay(self):
        self.switch_to_frame(store.readYaml('$.year.iframe.win', 1))

    @allure.step('切换到mac购买一年套餐弹窗')
    def switch_to_mac_year_pay(self):
        self.switch_to_frame(store.readYaml('$.year.iframe.mac', 1))

    @allure.step('切换到购买win永久一台弹窗')
    def switch_to_win_lifetime_one_pay(self):
        self.switch_to_frame(store.readYaml('$.lifetime-license.one.iframe.win', 1))

    @allure.step('切换到购买mac永久一台弹窗')
    def switch_to_mac_lifetime_one_pay(self):
        self.switch_to_frame(store.readYaml('$.lifetime-license.one.iframe.mac', 1))

    @allure.step('切换到购买win永久五台弹窗')
    def switch_to_win_lifetime_five_pay(self):
        self.switch_to_frame(store.readYaml('$.lifetime-license.five.iframe.win', 1))

    @allure.step('切换到购买mac永久五台弹窗')
    def switch_to_mac_lifetime_five_pay(self):
        self.switch_to_frame(store.readYaml('$.lifetime-license.five.iframe.mac', 1))

    def assert_win_month_pay(self):
        self.allure_assert('判断支付弹窗信息是否对应win一个月套餐', (
            'eq', self.element_text(store['pay-title']), getValueByIndex(1, 2, 'video-win套餐价格', 'Store/store.xlsx'),
            ('eq', self.element_text(store['pay-price']), "€" + str(
                "%.2f" % (float(getValueByIndex(3, 2, 'video-win套餐价格', 'Store/store.xlsx').split("$")[1]) * 1.19)))))

    def assert_win_year_pay(self):
        self.allure_assert('判断支付弹窗信息是否对应win一个年套餐', (
            'eq', self.element_text(store['pay-title']), getValueByIndex(1, 3, 'video-win套餐价格', 'Store/store.xlsx'),
            ('eq', self.element_text(store['pay-price']), "€" + str(
                "%.2f" % (float(getValueByIndex(3, 3, 'video-win套餐价格', 'Store/store.xlsx').split("$")[1]) * 1.19)))))

    def assert_win_lifetime_one_pay(self):
        self.allure_assert('判断支付弹窗信息是否对应win永久一台套餐', (
            'eq', self.element_text(store['pay-title']), getValueByIndex(1, 4, 'video-win套餐价格', 'Store/store.xlsx'),
            ('eq', self.element_text(store['pay-price']), "€" + str(
                "%.2f" % (float(getValueByIndex(3, 4, 'video-win套餐价格', 'Store/store.xlsx').split("$")[1]) * 1.19)))))

    def assert_win_lifetime_five_pay(self):
        self.allure_assert('判断支付弹窗信息是否对应win永久五台套餐', (
            'eq', self.element_text(store['pay-title']), getValueByIndex(1, 5, 'video-win套餐价格', 'Store/store.xlsx'),
            ('eq', self.element_text(store['pay-price']), "€" + str(
                "%.2f" % (float(getValueByIndex(3, 5, 'video-win套餐价格', 'Store/store.xlsx').split("$")[1]) * 1.19)))))

    def assert_mac_month_pay(self):
        self.allure_assert('判断支付弹窗信息是否对应mac一个月套餐', (
            'eq', self.element_text(store['pay-title']), getValueByIndex(1, 2, 'video-mac套餐价格', 'Store/store.xlsx'),
            ('eq', self.element_text(store['pay-price']), "€" + str(
                "%.2f" % (float(getValueByIndex(3, 2, 'video-mac套餐价格', 'Store/store.xlsx').split("$")[1]) * 1.19)))))

    def assert_mac_year_pay(self):
        self.allure_assert('判断支付弹窗信息是否对应mac一个年套餐', (
            'eq', self.element_text(store['pay-title']), getValueByIndex(1, 3, 'video-mac套餐价格', 'Store/store.xlsx'),
            ('eq', self.element_text(store['pay-price']), "€" + str(
                "%.2f" % (float(getValueByIndex(3, 3, 'video-mac套餐价格', 'Store/store.xlsx').split("$")[1]) * 1.19)))))

    def assert_mac_lifetime_one_pay(self):
        self.allure_assert('判断支付弹窗信息是否对应mac永久一台套餐', (
            'eq', self.element_text(store['pay-title']), getValueByIndex(1, 4, 'video-mac套餐价格', 'Store/store.xlsx'),
            ('eq', self.element_text(store['pay-price']), "€" + str(
                "%.2f" % (float(getValueByIndex(3, 4, 'video-mac套餐价格', 'Store/store.xlsx').split("$")[1]) * 1.19)))))

    def assert_mac_lifetime_five_pay(self):
        self.allure_assert('判断支付弹窗信息是否对应mac永久五台套餐', (
            'eq', self.element_text(store['pay-title']), getValueByIndex(1, 5, 'video-mac套餐价格', 'Store/store.xlsx'),
            ('eq', self.element_text(store['pay-price']), "€" + str(
                "%.2f" % (float(getValueByIndex(3, 5, 'video-mac套餐价格', 'Store/store.xlsx').split("$")[1]) * 1.19)))))

    @allure.step('展开所有faq')
    def click_unfold_faqs_button(self):
        faqs_button = self.find_elements(store['item-button'])
        for i in faqs_button:
            self.scroll_to_element(i)
            i.click()

    @allure.step('折叠所有faq')
    def click_fold_faqs_button(self):
        faqs_button = self.find_elements(store['item-button'])
        for i in faqs_button:
            self.scroll_to_element(i)
            i.click()

    def assert_faqs_fold(self):
        self.allure_assert('判断问题展开成功',
                           ('eq', self.getAttributes(store['item-desc'], 'class'), ['faqs-item-desc faqs-active'] * 5))

    def assert_faqs_unfold(self):
        self.allure_assert('判断问题折叠成功', ('eq', self.getAttributes(store['item-desc'], 'class'), ['faqs-item-desc'] * 5))
