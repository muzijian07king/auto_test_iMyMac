import allure
from pytest_project.page.basepage import WebPage
from pytest_project.common.readelement import Element
from pytest_project.common.readexcel import getValueByIndex
from decimal import Decimal
from pytest_project.utils.times import sleep

buy = Element('Store/buy')
index = Element('Store/store-index')


class BuyPage(WebPage):

    def assert_pmm_original_price(self):
        self.allure_assert('判断优惠前价格', ('eq', self.element_text(index.readYaml('$.price.pmm.original-price')),
                                       getValueByIndex(2, 2, 'pmm套餐价格', 'Store/store.xlsx')))

    def assert_pmm_now_price(self):
        self.allure_assert('判断优惠后价格', ('eq', self.element_text(index.readYaml('$.price.pmm.now-price')),
                                       getValueByIndex(3, 2, 'pmm套餐价格', 'Store/store.xlsx')))

    def assert_pmm_discounts_price(self):
        self.allure_assert('判断优惠价格', ('eq', self.element_text(index.readYaml('$.price.pmm.discounts-price')),
                                      getValueByIndex(4, 2, 'pmm套餐价格', 'Store/store.xlsx')))

    def assert_video_original_price(self):
        self.allure_assert('判断优惠前价格', ('eq', self.element_text(index.readYaml('$.price.pmm.original-price')),
                                       getValueByIndex(2, 2, 'video-mac套餐价格', 'Store/store.xlsx')))

    def assert_video_now_price(self):
        self.allure_assert('判断优惠后价格', ('eq', self.element_text(index.readYaml('$.price.pmm.now-price')),
                                       getValueByIndex(3, 2, 'video-mac套餐价格', 'Store/store.xlsx')))

    def assert_video_discounts_price(self):
        self.allure_assert('判断优惠价格', ('eq', self.element_text(index.readYaml('$.price.pmm.discounts-price')),
                                      getValueByIndex(4, 2, 'video-mac套餐价格', 'Store/store.xlsx')))

    @allure.step('单击购买pmm一个月套餐按钮')
    def click_buy_pmm_button(self):
        self.is_click(index.readYaml('$.buy.PowerMyMac'))

    @allure.step('单击购买video一个月套餐按钮')
    def click_buy_video_button(self):
        self.is_click(index.readYaml('$.buy.Video-Converter'))

    @allure.step('单击pmm更多选项按钮')
    def click_pmm_option_button(self):
        self.is_click(index['pmm-option'])

    @allure.step('单击video更多选项按钮')
    def click_video_option_button(self):
        self.is_click(index['video-option'])

    def assert_popup_buy(self):
        """判断是否弹出支付弹窗"""
        self.allure_assert('判断是否弹出支付弹窗', ('not_eq', self.find_element(index['iframe']), None))

    def scroll_pmm_option(self):
        """移动到pmm-option"""
        self.scroll_to_loc(index['pmm-option'])

    def scroll_video_option(self):
        """移动到video-option"""
        self.scroll_to_loc(index['video-option'])

    def assert_goto_pmm_option(self):
        """判断是否跳转pmm更多页面"""
        self.allure_assert('判断跳转pmm更多页面',
                           ('eq', self.get_current_url(), 'https://www.imymac.com/store/buy-powermymac.html'))

    def assert_goto_video_option(self):
        """判断是否跳转video更多页面"""
        self.allure_assert('判断跳转video更多页面',
                           ('eq', self.get_current_url(), 'https://www.imymac.com/store/buy-video-converter.html'))

    # =======================================================
    """buy页面"""

    @allure.step('切换到pmm的paypal弹窗')
    def switch_pmm_iframe(self):
        self.switch_to_frame('pf_655714')

    @allure.step('切换到video的paypal弹窗')
    def switch_video_iframe(self):
        self.switch_to_frame('pf_666252')

    @allure.step('进入购买第一步页面')
    def buy_first_step(self):
        sleep(0.5)
        self.select_by_value(buy['buy-language'], 'zh-Hans')

    @allure.step('进入购买第二步页面')
    def buy_two_step(self):
        self.buy_first_step()
        self.send_email('123@123.com')
        self.confirm_email()

    @allure.step('进入购买第三步页面')
    def buy_three_step(self):
        self.buy_two_step()
        self.region_select_by_value('CN')
        self.confirm_region()

    @allure.step('添加优惠码步骤')
    def buy_addCoupon_step(self, code):
        self.buy_three_step()
        self.click_add_coupon()
        self.send_coupon_code(code)
        self.submit_coupon()

    @allure.step('点击购买数量下拉框')
    def click_num_select(self):
        self.is_click(buy['num_select'])

    @allure.step('选择购买数量')
    def num_select(self, number):
        self.select_by_value(buy['num_select'], number)
        sleep(3)

    def assert_price(self, number):
        """对比价格"""
        if int(number) > 65535:
            number = '65535'
        # self.allure_assert('判断价格是否正确', ('eq', self.element_text(buy['price']).split('€')[1], "%.2f" % (9.95 * 1.19
        # * int(number))))
        self.allure_assert('判断价格是否正确', (
            'eq', Decimal(self.element_text(buy['price']).split('$')[1]), Decimal('9.95') * Decimal(number)))

    @allure.step('输入邮箱')
    def send_email(self, text):
        self.input_text(buy['send-email'], text)
        sleep(2)

    @allure.step('点击确认邮箱按钮')
    def confirm_email(self):
        self.is_click(buy.readYaml('$.next.one'))

    def assert_email_error_text(self, error):
        self.allure_assert('判断错误邮箱信息', ('eq', self.element_text(buy['email-error-text']), error))

    def assert_customer_email(self, email):
        self.allure_assert('判断用户邮箱填写是否成功', ('eq', self.element_text(buy['customer-email']), email))

    @allure.step('点击地区下拉框')
    def region_select(self):
        self.is_click(buy['region-select'])

    @allure.step('选择地区地区下拉框')
    def region_select_by_value(self, region):
        self.select_by_value(buy['region-select'], region)

    def assert_region_option_text(self, region):
        self.allure_assert('判断是否选中地区', ('eq', self.select_option_text(buy['region-select']), region))

    @allure.step('点击确认地区')
    def confirm_region(self):
        self.is_click(buy.readYaml('$.next.two'))

    def assert_goto_region_page(self):
        self.allure_assert('判断是否进入填写地区页面', ('not_eq', self.find_element(buy['region-select']), None))

    def assert_goto_pay_page(self):
        self.allure_assert('判断是否进入选择支付方式页面', ('not_eq', self.find_element(buy['addCouponButton']), None))

    @allure.step('点击添加优惠卷链接')
    def click_add_coupon(self):
        self.is_click(buy['addCouponButton'])

    @allure.step('输入优惠码')
    def send_coupon_code(self, text):
        self.input_text(buy['couponCodeInput'], text)

    @allure.step('提交优惠码')
    def submit_coupon(self):
        self.is_click(buy['submitCouponButton'])

    def assert_code_error_text(self, error):
        self.allure_assert('判断优惠码错误信息', ('eq', self.element_text(buy['notification']), error))

    def assert_code_null_text(self, error):
        self.allure_assert('判断优惠码为空错误信息', ('eq', self.element_text(buy['codeNotification']), error))

    @allure.step('取消添加优惠码')
    def cancel_coupon(self):
        self.is_click(buy['cancelCouponButton'])

    def assert_cancel_pay(self):
        self.allure_assert('判断是否取消支付', ('not_eq', self.find_element(buy['paypal']), None))

    @allure.step('移除优惠码')
    def click_delete_coupon(self):
        self.is_click(buy['delete-conpon'], 1)

    def assert_delete_coupon(self):
        self.allure_assert('判断是否删除优惠券', ('not_eq', self.find_element(buy['delete-conpon']), None))

    def assert_after_discount_price(self, discount=1):
        """
        断言优惠后的价格,价格要用decimal进行计算
        """
        self.allure_assert('判断优惠后的价格是否正确', (
            'eq', Decimal(self.element_text(buy['product-price']).split('$')[1]), Decimal('9.95') * Decimal(
                discount)))

    @allure.step('点击修改邮箱按钮')
    def click_update_email(self):
        self.is_click(buy['update-email'])

    def assert_again_send_email(self):
        """判断进入填写邮箱页面"""
        self.allure_assert('判断是否进入填写邮箱页面', ('not_eq', self.find_element(buy['send-email']), None))

    @allure.step('选择卡片支付')
    def card_to_pay(self):
        self.is_click(buy['card-pay'])
        sleep(2)

    @allure.step('选择paypal支付')
    def paypal_to_pay(self):
        self.is_click(buy['paypal'])

    @allure.step('输入卡号')
    def send_cardNumber(self, number):
        self.input_text(buy['cardNumber'], number)

    @allure.step('输入持卡人')
    def send_cardName(self, name):
        self.input_text(buy['cardName'], name)

    @allure.step('输入截至月')
    def send_cardMonth(self, month):
        self.input_text(buy['cardMonth'], month)

    @allure.step('输入截至年')
    def send_cardYear(self, year):
        self.input_text(buy['cardYear'], year)

    @allure.step('输入安全码')
    def send_cardPwd(self, pwd):
        self.input_text(buy['cardPwd'], pwd)

    @allure.step('提交输入卡信息')
    def submit_card(self):
        self.is_click(buy['cardSubmit'], 1)

    @allure.step('点击使用其他支付方式按钮')
    def cancel_pay(self):
        self.is_click(buy['cancel-pay'])

    @allure.step('点击使用其他支付方式')
    def cancel_paypal_pay(self):
        self.is_click(buy['cancel-paypal-pay'])

    @allure.step('关闭支付')
    def close_pay(self):
        self.is_click(buy['close-pay'])

    def assert_close(self):
        self.allure_assert('判断是否关闭支付页面', ('not_eq', self.find_element(('tag', 'iframe')), None))

    def assert_goto_paypal(self):
        self.allure_assert('判断弹出PayPal支付页面', ('not_eq', self.find_element(buy['load-paypal']), None))

    def assert_card_pay_error_texts(self, error):
        self.allure_assert('判断卡支付错误信息', ('eq', ''.join(self.elements_text(buy['card-pay-texts'])), error))

    # def return_card_pay_bank_safe_texts(self):
    #     result = self.element_text(buy['bank-safe'])
    #     self.allure_assert_step('判断卡支付银行安全提醒', result)
    #     return result

    def assert_card_pay_BANK_error_text(self, error):
        self.allure_assert('判断卡支付银行拒绝错误信息', ('include', error, self.element_text(buy['card-pay-BANK-error'])))
