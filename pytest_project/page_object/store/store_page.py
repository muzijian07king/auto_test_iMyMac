import allure

from pytest_project.page.basepage import WebPage
from pytest_project.common.readelement import Element, get_any_key_info, get_values_in_name
from decimal import Decimal
from pytest_project.utils.times import sleep

store = Element('Store/body')


class StorePage(WebPage):

    @allure.step('点击购买按钮')
    def click_buy(self, loc):
        self.is_click(loc)
        sleep()

    @allure.step('进入购买ppm第一步页面')
    def pmm_buy_first_step(self):
        self.is_click(get_values_in_name().get_values_in_name(store.data, 'buy-button')[0])
        self.switch_to_pmm()
        self.select_by_value(store['language'], 'zh-Hans')

    @allure.step('进入购买ppm第二步页面')
    def pmm_buy_two_step(self):
        self.pmm_buy_first_step()
        self.send_email('123@123.com')
        self.confirm_email()

    @allure.step('进入购买ppm第三步页面')
    def pmm_buy_three_step(self):
        self.pmm_buy_two_step()
        self.region_select('CN')
        self.confirm_region()

    @allure.step('添加pmm优惠码步骤')
    def pmm_buy_addCoupon_step(self, code):
        self.pmm_buy_three_step()
        self.click_add_coupon()
        self.send_coupon_code(code)
        self.submit_coupon()

    @allure.step('添加video优惠码步骤')
    def video_buy_addCoupon_step(self, code):
        self.video_buy_three_step()
        self.click_add_coupon()
        self.send_coupon_code(code)
        self.submit_coupon()

    @allure.step('进入购买video第一步页面')
    def video_buy_first_step(self):
        self.is_click(get_values_in_name().get_values_in_name(store.data, 'buy-button')[1])
        self.switch_to_video()
        self.select_by_value(store['language'], 'zh-Hans')

    @allure.step('进入购买video第二步页面')
    def video_buy_two_step(self):
        self.video_buy_first_step()
        self.send_email('123@123.com')
        self.confirm_email()

    @allure.step('进入购买video第三步页面')
    def video_buy_three_step(self):
        self.video_buy_two_step()
        self.region_select('CN')
        self.confirm_region()

    @allure.step('添加video优惠码步骤')
    def video_buy_addCoupon_step(self, code):
        self.video_buy_three_step()
        self.click_add_coupon()
        self.send_coupon_code(code)
        self.submit_coupon()

    @allure.step('点击更多按钮')
    def click_video_option(self):
        self.is_click(get_values_in_name().get_values_in_name(store.data, 'options')[1])

    @allure.step('点击更多按钮')
    def click_pmm_option(self):
        self.is_click(get_values_in_name().get_values_in_name(store.data, 'options')[0])

    @allure.step('切换到pmm购买页面')
    def switch_to_pmm(self):
        self.switch_to_frame('pf_631115')

    @allure.step('切换到video购买页面')
    def switch_to_video(self):
        self.switch_to_frame('pf_588082')

    def is_buy(self):
        with allure.step('判断是否弹出支付页面'):
            return self.find_element(store['iframe']) is not None

    def is_video_buy(self):
        with allure.step('判断是否进入支付页面'):
            self.switch_to_video()
            return self.find_element(store['send-email']) is not None

    def is_pmm_buy(self):
        with allure.step('判断是否进入支付页面'):
            self.switch_to_pmm()
            return self.find_element(store['send-email']) is not None

    def is_again_send_email(self):
        with allure.step('是否跳转到填写邮箱页面'):
            return self.find_element(store['send-email']) is not None

    @allure.step('输入邮箱')
    def send_email(self, text):
        self.input_text(store['send-email'], text)

    @allure.step('点击确认邮箱按钮')
    def confirm_email(self):
        self.is_click(get_any_key_info(1, store.data))

    @allure.step('点击地区下拉框')
    def region_select(self, language):
        self.select_by_value(store['region-select'], language)

    @allure.step('点击地区下拉框')
    def region_select_by_index(self, index):
        self.select_by_index(store['region-select'], index)

    @allure.step('将空地区变成可选')
    def js_disable_into_none(self):
        self.jsInDriver('document.querySelector("#countryCode > option:nth-child(1)").disabled=""')

    def return_region_option_text(self, region):
        with allure.step('判断是否选中地区'):
            return self.select_option_text(store['region-select']) == region

    def return_region_null_error_text(self):
        with allure.step('判断是否可填写空地区'):
            return self.element_txet(store['region-error-text']) == '必须填写国家/地区。'

    @allure.step('点击购买数量下拉框')
    def num_select(self, number):
        self.select_by_value(store['num_select'], number)
        sleep(3)

    @allure.step('点击确认地区')
    def confirm_region(self):
        self.is_click(get_any_key_info(2, store.data))

    def return_email_error_text(self):
        with allure.step('判断错误邮箱信息'):
            return self.element_txet(store['email-error-text'])

    def is_goto_region_page(self):
        with allure.step('判断是否进入填写地区页面'):
            return self.find_element(store['region-select']) is not None

    def return_pmm_price(self, number):
        """双精度对比价格"""
        with allure.step('判断pmm价格是否正确'):
            return Decimal(self.element_txet(store['price']).split('$')[1]) == Decimal('9.95') * Decimal(number)

    def return_video_price(self, number):
        """双精度对比价格"""
        with allure.step('判断video价格是否正确'):
            return Decimal(self.element_txet(store['price']).split('$')[1]) == Decimal('19.95') * Decimal(number)

    def return_customer_email(self):
        with allure.step('判断用户邮箱填写是否成功'):
            return self.element_txet(store['customer-email'])

    def return_product_price(self):
        with allure.step('判断商品价格是否正确'):
            return self.element_txet(store['product-price']).split('$')[1]

    def return_pmm_after_discount_price(self, discount=1):
        """
        断言优惠后的价格,价格要用decimal进行计算
        """
        with allure.step('判断优惠后的价格是否正确'):
            return Decimal(self.element_txet(store['product-price']).split('$')[1]) == Decimal('9.95') * Decimal(
                discount)

    def return_video_after_discount_price(self, discount=1):
        with allure.step('判断优惠后价格是否正确'):
            return Decimal(self.element_txet(store['product-price']).split('$')[1]) == Decimal('19.95') * Decimal(
                discount)

    def is_cancel_pay(self):
        with allure.step('判断是否取消支付'):
            return self.find_element(store['paypal']) is not None

    @allure.step('点击修改邮箱按钮')
    def click_update_email(self):
        self.is_click(store['update-email'])

    @allure.step('点击添加优惠卷链接')
    def click_add_coupon(self):
        self.is_click(store['addCouponButton'])

    @allure.step('输入优惠码')
    def send_coupon_code(self, text):
        self.input_text(store['couponCodeInput'], text)

    @allure.step('提交优惠码')
    def submit_coupon(self):
        self.is_click(store['submitCouponButton'])

    def return_code_error_text(self):
        with allure.step('判断优惠码错误信息'):
            return self.element_txet(store['notification'])

    def return_code_null_text(self):
        with allure.step('判断优惠码为空错误信息'):
            return self.element_txet(store['codeNotification'])

    @allure.step('取消添加优惠码')
    def cancel_coupon(self):
        self.is_click(store['cancelCouponButton'])

    @allure.step('移除优惠码')
    def click_delete_coupon(self):
        self.is_click(store['delete-conpon'])

    @allure.step('选择卡片支付')
    def card_to_pay(self):
        self.is_click(store['card-pay'])
        sleep(2)

    @allure.step('选择paypal支付')
    def paypal_to_pay(self):
        self.is_click(store['paypal'])

    @allure.step('输入卡号')
    def send_cardNumber(self, number):
        self.input_text(store['cardNumber'], number)

    @allure.step('输入持卡人')
    def send_cardName(self, name):
        self.input_text(store['cardName'], name)

    @allure.step('输入截至月')
    def send_cardMonth(self, month):
        self.input_text(store['cardMonth'], month)

    @allure.step('输入截至年')
    def send_cardYear(self, year):
        self.input_text(store['cardYear'], year)

    @allure.step('输入安全码')
    def send_cardPwd(self, pwd):
        self.input_text(store['cardPwd'], pwd)

    @allure.step('提交输入卡信息')
    def submit_card(self):
        self.is_click(store['cardSubmit'])

    @allure.step('点击使用其他支付方式按钮')
    def cancel_pay(self):
        self.is_click(store['cancel-pay'])

    @allure.step('点击使用其他支付方式')
    def cancel_paypal_pay(self):
        self.is_click(store['cancel-paypal-pay'])

    @allure.step('关闭支付')
    def close_pay(self):
        self.is_click(store['close-pay'])

    def is_close(self):
        with allure.step('判断是否关闭支付页面'):
            return self.find_element(('tag', 'iframe')) is None

    def is_goto_paypal(self):
        with allure.step('判断弹出PayPal支付页面'):
            return self.find_element(store['load-paypal']) is not None

    def is_option(self, handle):
        return self.element_txet(store['buy-handle']) == handle

    def return_card_pay_error_texts(self):
        with allure.step('判断卡支付错误信息'):
            return self.elements_text(store['card-pay-texts'])

    def return_card_pay_bank_safe_texts(self):
        with allure.step("判断卡支付银行安全提醒"):
            return self.element_txet(store['bank-safe'])

    def return_card_pay_BANK_error_text(self):
        with allure.step('判断卡支付银行拒绝错误信息'):
            return self.element_txet(store['card-pay-BANK-error'])
