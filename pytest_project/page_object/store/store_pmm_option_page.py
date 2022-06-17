import allure

from pytest_project.page.basepage import WebPage
from pytest_project.common.readelement import Element
from pytest_project.common.readexcel import getValueByIndex

store = Element('Store/pmm-store-option')


class OptionPage(WebPage):
    def assert_month_original_price(self):
        self.allure_assert('判断产品购买一个月原价', ('eq', self.element_text(store.readYaml('$.month.original-price')),
                                           getValueByIndex(2, 2, 'pmm套餐价格', 'Store/store.xlsx')))

    def assert_month_now_price(self):
        self.allure_assert('判断产品购买一个月现价', ('eq', self.element_text(store.readYaml('$.month.now-price')),
                                           getValueByIndex(3, 2, 'pmm套餐价格', 'Store/store.xlsx')))

    def assert_month_discounts_price(self):
        self.allure_assert('判断产品购买一个月优惠价', ('eq', self.element_text(store.readYaml('$.month.discounts-price')),
                                            getValueByIndex(4, 2, 'pmm套餐价格', 'Store/store.xlsx')))

    def assert_year_one_original_price(self):
        self.allure_assert('判断产品购买一个年一台原价', ('eq', self.element_text(store.readYaml('$.year.1-Mac.original-price')),
                                             getValueByIndex(2, 3, 'pmm套餐价格', 'Store/store.xlsx')))

    def assert_year_one_now_price(self):
        self.allure_assert('判断产品购买一个年一台年现价', ('eq', self.element_text(store.readYaml('$.year.1-Mac.now-price')),
                                              getValueByIndex(3, 3, 'pmm套餐价格', 'Store/store.xlsx')))

    def assert_year_one_discounts_price(self):
        self.allure_assert('判断产品购买一个年一台优惠价', ('eq', self.element_text(store.readYaml('$.year.1-Mac.discounts-price')),
                                              getValueByIndex(4, 3, 'pmm套餐价格', 'Store/store.xlsx')))

    def assert_year_two_original_price(self):
        self.allure_assert('判断产品购买一个年两个设备原价', ('eq', self.element_text(store.readYaml('$.year.2-Macs.original-price')),
                                               getValueByIndex(2, 4, 'pmm套餐价格', 'Store/store.xlsx')))

    def assert_year_two_now_price(self):
        self.allure_assert('判断产品购买一个年两个设备现价', ('eq', self.element_text(store.readYaml('$.year.2-Macs.now-price')),
                                               getValueByIndex(3, 4, 'pmm套餐价格', 'Store/store.xlsx')))

    def assert_year_two_discounts_price(self):
        self.allure_assert('判断产品购买一个年两个设备优惠价',
                           ('eq', self.element_text(store.readYaml('$.year.2-Macs.discounts-price')),
                            getValueByIndex(4, 4, 'pmm套餐价格', 'Store/store.xlsx')))

    def assert_year_five_original_price(self):
        self.allure_assert('判断产品购买一个年五台设备原价', ('eq', self.element_text(store.readYaml('$.year.5-Macs.original-price')),
                                               getValueByIndex(2, 5, 'pmm套餐价格', 'Store/store.xlsx')))

    def assert_year_five_now_price(self):
        self.allure_assert('判断产品购买一个年五台设备现价', ('eq', self.element_text(store.readYaml('$.year.5-Macs.now-price')),
                                               getValueByIndex(3, 5, 'pmm套餐价格', 'Store/store.xlsx')))

    def assert_year_five_discounts_price(self):
        self.allure_assert('判断产品购买一个年五台设备优惠价',
                           ('eq', self.element_text(store.readYaml('$.year.5-Macs.discounts-price')),
                            getValueByIndex(4, 5, 'pmm套餐价格', 'Store/store.xlsx')))

    def assert_lifetime_one_original_price(self):
        self.allure_assert('判断产品购买永久一台设备原价', (
            'eq', self.element_text(store.readYaml('$.lifetime-license.1-Mac.original-price')),
            getValueByIndex(2, 6, 'pmm套餐价格', 'Store/store.xlsx')))

    def assert_lifetime_one_now_price(self):
        self.allure_assert('判断产品购买永久一台设备现价', (
            'eq', self.element_text(store.readYaml('$.lifetime-license.1-Mac.now-price')),
            getValueByIndex(3, 6, 'pmm套餐价格', 'Store/store.xlsx')))

    def assert_lifetime_one_discounts_price(self):
        self.allure_assert('判断产品购买永久一台设备优惠价', (
            'eq', self.element_text(store.readYaml('$.lifetime-license.1-Mac.discounts-price')),
            getValueByIndex(4, 6, 'pmm套餐价格', 'Store/store.xlsx')))

    def assert_lifetime_two_original_price(self):
        self.allure_assert('判断产品购买永久两台设备原价', (
            'eq', self.element_text(store.readYaml('$.lifetime-license.2-Macs.original-price')),
            getValueByIndex(2, 7, 'pmm套餐价格', 'Store/store.xlsx')))

    def assert_lifetime_two_now_price(self):
        self.allure_assert('判断产品购买永久两台设备现价', (
            'eq', self.element_text(store.readYaml('$.lifetime-license.2-Macs.now-price')),
            getValueByIndex(3, 7, 'pmm套餐价格', 'Store/store.xlsx')))

    def assert_lifetime_two_discounts_price(self):
        self.allure_assert('判断产品购买永久两台设备优惠价', (
            'eq', self.element_text(store.readYaml('$.lifetime-license.2-Macs.discounts-price')),
            getValueByIndex(4, 7, 'pmm套餐价格', 'Store/store.xlsx')))

    def assert_lifetime_five_original_price(self):
        self.allure_assert('判断产品购买永久五台设备原价', (
            'eq', self.element_text(store.readYaml('$.lifetime-license.5-Macs.original-price')),
            getValueByIndex(2, 8, 'pmm套餐价格', 'Store/store.xlsx')))

    def assert_lifetime_five_now_price(self):
        self.allure_assert('判断产品购买永久五台设备现价', (
            'eq', self.element_text(store.readYaml('$.lifetime-license.5-Macs.now-price')),
            getValueByIndex(3, 8, 'pmm套餐价格', 'Store/store.xlsx')))

    def assert_lifetime_five_discounts_price(self):
        self.allure_assert('判断产品购买永久五台设备优惠价', (
            'eq', self.element_text(store.readYaml('$.lifetime-license.5-Macs.discounts-price')),
            getValueByIndex(4, 8, 'pmm套餐价格', 'Store/store.xlsx')))

    @allure.step("点击购买一个月套餐按钮")
    def click_buy_month_button(self):
        self.is_click(store.readYaml('$.month.buy'))

    @allure.step("切换到一年一台套餐")
    def switch_to_year_one_button(self):
        self.is_click(store.readYaml("$.year.1-Mac.option"))

    @allure.step("点击购买一年一台套餐按钮")
    def click_buy_year_one_button(self):
        self.is_click(store.readYaml('$.year.1-Mac.buy'))

    @allure.step("切换到一年两台套餐")
    def switch_to_year_two_button(self):
        self.is_click(store.readYaml("$.year.2-Macs.option"))

    @allure.step("切换到一年五台套餐")
    def switch_to_year_five_button(self):
        self.is_click(store.readYaml("$.year.5-Macs.option"))

    @allure.step("点击购买一年两台套餐按钮")
    def click_buy_year_two_button(self):
        self.is_click(store.readYaml('$.year.2-Macs.buy'))

    @allure.step("点击购买一年五台套餐按钮")
    def click_buy_year_five_button(self):
        self.is_click(store.readYaml('$.year.5-Macs.buy'))

    @allure.step('切换到永久一台套餐')
    def switch_to_lifetime_one_button(self):
        self.is_click(store.readYaml('$.lifetime-license.1-Mac.option'))

    @allure.step('切换到永久两台套餐')
    def switch_to_lifetime_two_button(self):
        self.is_click(store.readYaml('$.lifetime-license.2-Macs.option'))

    @allure.step('切换到永久五台套餐')
    def switch_to_lifetime_five_button(self):
        self.is_click(store.readYaml('$.lifetime-license.5-Macs.option'))

    @allure.step('点击购买永久一台套餐按钮')
    def click_buy_lifetime_one_button(self):
        self.is_click(store.readYaml('$.lifetime-license.1-Mac.buy'))

    @allure.step('点击购买永久两台套餐按钮')
    def click_buy_lifetime_two_button(self):
        self.is_click(store.readYaml('$.lifetime-license.2-Macs.buy'))

    @allure.step('点击购买永久五台套餐按钮')
    def click_buy_lifetime_five_button(self):
        self.is_click(store.readYaml('$.lifetime-license.5-Macs.buy'))

    @allure.step('切换到一个月套餐购买弹窗')
    def switch_to_month_pay(self):
        self.switch_to_frame(store.readYaml('$.month.iframe', 1))

    @allure.step('切换到一年一台套餐购买弹窗')
    def switch_to_year_one_pay(self):
        self.switch_to_frame(store.readYaml('$.year.1-Mac.iframe', 1))

    @allure.step('切换到一年两台套餐购买弹窗')
    def switch_to_year_two_pay(self):
        self.switch_to_frame(store.readYaml('$.year.2-Macs.iframe', 1))

    @allure.step('切换到一年五台套餐购买弹窗')
    def switch_to_year_five_pay(self):
        self.switch_to_frame(store.readYaml('$.year.5-Macs.iframe', 1))

    @allure.step('切换到永久一台套餐购买弹窗')
    def switch_to_lifetime_one_pay(self):
        self.switch_to_frame(store.readYaml('$.lifetime-license.1-Mac.iframe', 1))

    @allure.step('切换到永久两台套餐购买弹窗')
    def switch_to_lifetime_two_pay(self):
        self.switch_to_frame(store.readYaml('$.lifetime-license.2-Macs.iframe', 1))

    @allure.step('切换到永久五台套餐购买弹窗')
    def switch_to_lifetime_five_pay(self):
        self.switch_to_frame(store.readYaml('$.lifetime-license.5-Macs.iframe', 1))

    def assert_month_pay(self):
        # self.allure_assert('判断支付弹窗信息是否对应一个月套餐', (
        #     'eq', self.element_text(store['pay-title']), getValueByIndex(1, 2, 'pmm套餐价格', 'Store/store.xlsx')),
        #                    ('eq', self.element_text(store['pay-price']), "€" + str(
        #                        "%.2f" % (float(
        #                            getValueByIndex(3, 2, 'pmm套餐价格', 'Store/store.xlsx').split("$")[1]) * 1.19))))
        self.allure_assert('判断支付弹窗信息是否对应一个月套餐', (
            'eq', self.element_text(store['pay-title']), getValueByIndex(1, 2, 'pmm套餐价格', 'Store/store.xlsx')),
                           ('eq', self.element_text(store['pay-price']).split('$')[1],
                            getValueByIndex(3, 2, 'pmm套餐价格', 'Store/store.xlsx').split("$")[1]))

    def assert_year_one_pay(self):
        # self.allure_assert('判断支付弹窗信息是否对应一个年一台套餐', (
        #     'eq', self.element_text(store['pay-title']), getValueByIndex(1, 3, 'pmm套餐价格', 'Store/store.xlsx')),
        #                    ('eq', self.element_text(store['pay-price']), "€" + str(
        #                        "%.2f" % (float(
        #                            getValueByIndex(3, 3, 'pmm套餐价格', 'Store/store.xlsx').split("$")[1]) * 1.19))))
        self.allure_assert('判断支付弹窗信息是否对应一个年一台套餐', (
            'eq', self.element_text(store['pay-title']), getValueByIndex(1, 3, 'pmm套餐价格', 'Store/store.xlsx')),
                           ('eq', self.element_text(store['pay-price']).split('$')[1],
                            getValueByIndex(3, 3, 'pmm套餐价格', 'Store/store.xlsx').split("$")[1]))

    def assert_year_two_pay(self):
        # self.allure_assert('判断支付弹窗信息是否对应一年两台套餐', (
        #     'eq', self.element_text(store['pay-title']), getValueByIndex(1, 4, 'pmm套餐价格', 'Store/store.xlsx')),
        #                    ('eq', self.element_text(store['pay-price']), "€" + str(
        #                        "%.2f" % (float(
        #                            getValueByIndex(3, 4, 'pmm套餐价格', 'Store/store.xlsx').split("$")[1]) * 1.19))))
        self.allure_assert('判断支付弹窗信息是否对应一年两台套餐', (
            'eq', self.element_text(store['pay-title']), getValueByIndex(1, 4, 'pmm套餐价格', 'Store/store.xlsx')),
                           ('eq', self.element_text(store['pay-price']).split('$')[1],
                            getValueByIndex(3, 4, 'pmm套餐价格', 'Store/store.xlsx').split("$")[1]))

    def assert_year_five_pay(self):
        # self.allure_assert('判断支付弹窗信息是否对应一年五台套餐', (
        #     'eq', self.element_text(store['pay-title']), getValueByIndex(1, 5, 'pmm套餐价格', 'Store/store.xlsx')),
        #                    ('eq', self.element_text(store['pay-price']), "€" + str(
        #                        "%.2f" % (float(
        #                            getValueByIndex(3, 5, 'pmm套餐价格', 'Store/store.xlsx').split("$")[1]) * 1.19))))
        self.allure_assert('判断支付弹窗信息是否对应一年五台套餐', (
            'eq', self.element_text(store['pay-title']), getValueByIndex(1, 5, 'pmm套餐价格', 'Store/store.xlsx')),
                           ('eq', self.element_text(store['pay-price']).split('$')[1],
                            getValueByIndex(3, 5, 'pmm套餐价格', 'Store/store.xlsx').split("$")[1]))

    def assert_lifetime_one_pay(self):
        # self.allure_assert('判断支付弹窗信息是否对应永久一台套餐', (
        #     'eq', self.element_text(store['pay-title']), getValueByIndex(1, 6, 'pmm套餐价格', 'Store/store.xlsx')),
        #                    ('eq', self.element_text(store['pay-price']), "€" + str(
        #                        "%.2f" % (float(
        #                            getValueByIndex(3, 6, 'pmm套餐价格', 'Store/store.xlsx').split("$")[1]) * 1.19))))
        self.allure_assert('判断支付弹窗信息是否对应永久一台套餐', (
            'eq', self.element_text(store['pay-title']), getValueByIndex(1, 6, 'pmm套餐价格', 'Store/store.xlsx')),
                           ('eq', self.element_text(store['pay-price']).split('$')[1],
                            getValueByIndex(3, 6, 'pmm套餐价格', 'Store/store.xlsx').split("$")[1]))

    def assert_lifetime_two_pay(self):
        # self.allure_assert('判断支付弹窗信息是否对应永久两台套餐', (
        #     'eq', self.element_text(store['pay-title']), getValueByIndex(1, 7, 'pmm套餐价格', 'Store/store.xlsx')),
        #                    ('eq', self.element_text(store['pay-price']), "€" + str(
        #                        "%.2f" % (float(
        #                            getValueByIndex(3, 7, 'pmm套餐价格', 'Store/store.xlsx').split("$")[1]) * 1.19))))
        self.allure_assert('判断支付弹窗信息是否对应永久两台套餐', (
            'eq', self.element_text(store['pay-title']), getValueByIndex(1, 7, 'pmm套餐价格', 'Store/store.xlsx')),
                           ('eq', self.element_text(store['pay-price']).split('$')[1],
                            getValueByIndex(3, 7, 'pmm套餐价格', 'Store/store.xlsx').split("$")[1]))

    def assert_lifetime_five_pay(self):
        # self.allure_assert('判断支付弹窗信息是否对应永久五台套餐', (
        #     'eq', self.element_text(store['pay-title']), getValueByIndex(1, 8, 'pmm套餐价格', 'Store/store.xlsx')),
        #                    ('eq', self.element_text(store['pay-price']), "€" + str(
        #                        "%.2f" % (float(
        #                            getValueByIndex(3, 8, 'pmm套餐价格', 'Store/store.xlsx').split("$")[1]) * 1.19))))
        self.allure_assert('判断支付弹窗信息是否对应永久五台套餐', (
            'eq', self.element_text(store['pay-title']), getValueByIndex(1, 8, 'pmm套餐价格', 'Store/store.xlsx')),
                           ('eq', self.element_text(store['pay-price']).split('$')[1],
                            getValueByIndex(3, 8, 'pmm套餐价格', 'Store/store.xlsx').split("$")[1]))

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

    @allure.step('判断是否存在优惠活动')
    def assert_discounts_popup(self):
        if self.find_element(store.readYaml('$.discounts-popup.popup')) is not None:
            self.is_click(store.readYaml('$.discounts-popup.close'))
