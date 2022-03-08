import allure
import pytest

from pytest_project.common.readexcel import getExcelAllData, getExcelOneCol, getExcelByRow
from pytest_project.page_object.store.store_index_page import BuyPage
from pytest_project.common.readconfig import ini


@allure.severity('critical')
@allure.feature('Store测试')
@allure.story('Store主页面内容测试')
class TestBody(object):
    @pytest.fixture(scope='function', autouse=True)
    def open_url(self, drivers):
        self.driver = BuyPage(drivers)
        self.driver.get_url(ini.get_url('store'))

    @allure.title('ppm一个月套餐优惠前价格测试')
    def test_001(self):
        """ppm一个月套餐优惠前价格测试"""
        allure.dynamic.tag('优惠前价格')
        self.driver.assert_pmm_original_price()

    @allure.title('ppm一个月套餐优惠后价格测试')
    def test_002(self):
        """ppm一个月套餐优惠后价格测试"""
        allure.dynamic.tag('优惠后价格')
        self.driver.assert_pmm_now_price()

    @allure.title('ppm一个月套餐优惠价格测试')
    def test_003(self):
        """ppm一个月套餐优惠价格测试"""
        allure.dynamic.tag('优惠价格')
        self.driver.assert_pmm_discounts_price()

    @allure.title('video一个月套餐优惠前价格测试')
    def test_004(self):
        """video一个月套餐优惠前价格测试"""
        allure.dynamic.tag('优惠前价格')
        self.driver.assert_video_original_price()

    @allure.title('ppm一个月套餐优惠后价格测试')
    def test_005(self):
        """video一个月套餐优惠后价格测试"""
        allure.dynamic.tag('优惠后价格')
        self.driver.assert_video_now_price()

    @allure.title('video一个月套餐优惠价格测试')
    def test_006(self):
        """video一个月套餐优惠价格测试"""
        allure.dynamic.tag('优惠价格')
        self.driver.assert_video_discounts_price()

    @allure.title('购买pmm一个月套餐测试')
    def test_007(self):
        """购买pmm一个月套餐功能测试"""
        allure.dynamic.tag('购买pmm')
        self.driver.click_buy_pmm_button()
        self.driver.assert_popup_buy()

    @allure.title('购买video一个月套餐测试')
    def test_008(self):
        """购买video一个月套餐功能测试"""
        allure.dynamic.tag('购买video')
        self.driver.click_buy_video_button()
        self.driver.assert_popup_buy()

    @allure.title('跳转pmm更多选项页面测试')
    def test_009(self):
        """跳转pmm更多选项页面测试"""
        allure.dynamic.tag('pmm更多选项')
        self.driver.scroll_pmm_option()
        self.driver.click_pmm_option_button()
        self.driver.assert_goto_pmm_option()

    @allure.title('跳转video更多选项页面测试')
    def test_010(self):
        """跳转video更多选项页面测试"""
        allure.dynamic.tag('video更多选项')
        self.driver.scroll_video_option()
        self.driver.click_video_option_button()
        self.driver.assert_goto_video_option()

    @pytest.mark.parametrize('number', ['1', '2', '3', '5', '10', '25'])
    @allure.title('pmm购买页面填写购买数量测试')
    def test_011(self, number):
        """pmm购买页面填写购买数量功能测试"""
        allure.dynamic.tag('购买数量为==》{}'.format(number))
        self.driver.click_buy_pmm_button()
        self.driver.switch_pmm_iframe()
        self.driver.buy_first_step()
        self.driver.click_num_select()
        self.driver.num_select(number)
        self.driver.assert_price(number)

    @pytest.mark.parametrize('email_data, error_text', getExcelAllData('邮箱错误', 'Store/store.xlsx'))
    @allure.title('pmm购买页面填写错误格式邮箱测试')
    @allure.severity('normal')
    def test_012(self, email_data, error_text):
        """pmm购买页面填写错误格式邮箱功能测试"""
        allure.dynamic.tag('邮箱为==》{}'.format(email_data))
        self.driver.click_buy_pmm_button()
        self.driver.switch_pmm_iframe()
        self.driver.buy_first_step()
        self.driver.send_email(' ')
        self.driver.confirm_email()
        self.driver.send_email(email_data)
        self.driver.confirm_email()
        self.driver.assert_email_error_text(error_text)

    @pytest.mark.parametrize('email_data', getExcelOneCol('邮箱正确', 1, 'Store/store.xlsx'))
    @allure.title('pmm购买页面填写正确格式邮箱测试')
    def test_013(self, email_data):
        """pmm购买页面填写正确格式邮箱功能测试"""
        allure.dynamic.tag('邮箱为==》{}'.format(email_data))
        self.driver.click_buy_pmm_button()
        self.driver.switch_pmm_iframe()
        self.driver.buy_first_step()
        self.driver.send_email(email_data)
        self.driver.confirm_email()
        self.driver.assert_goto_region_page() and self.driver.assert_customer_email(email_data)

    @pytest.mark.parametrize('region, language', getExcelAllData('语言简写', 'Store/store.xlsx'))
    @allure.title('pmm购买页面填写地区测试')
    def test_014(self, region, language):
        """pmm购买页面填写地区功能测试"""
        allure.dynamic.tag('地区选择==》{}'.format(language))
        self.driver.click_buy_pmm_button()
        self.driver.switch_pmm_iframe()
        self.driver.buy_two_step()
        self.driver.region_select()
        self.driver.region_select_by_value(region)
        self.driver.assert_region_option_text(language)

    @allure.title('pmm购买页面提交地区测试')
    def test_015(self):
        """pmm购买页面提交地区功能测试"""
        allure.dynamic.tag('提交地区')
        self.driver.click_buy_pmm_button()
        self.driver.switch_pmm_iframe()
        self.driver.buy_three_step()
        self.driver.assert_goto_pay_page()

    @allure.title('pmm购买页面重新填写邮箱测试')
    def test_016(self):
        """pmm购买页面重新填写邮箱功能测试"""
        allure.dynamic.tag('更改邮箱')
        self.driver.click_buy_pmm_button()
        self.driver.switch_pmm_iframe()
        self.driver.buy_two_step()
        self.driver.click_update_email()
        self.driver.assert_again_send_email()

    @pytest.mark.parametrize('code, error_text', getExcelByRow('优惠码错误', 1, 1, 'Store/store.xlsx'))
    @allure.title('pmm购买页面填写错误优惠码测试')
    def test_017(self, code, error_text):
        """pmm购买页面填写错误优惠码功能测试"""
        allure.dynamic.tag('优惠码==》{}'.format(code))
        self.driver.click_buy_pmm_button()
        self.driver.switch_pmm_iframe()
        self.driver.buy_addCoupon_step(code)
        self.driver.assert_code_error_text(error_text)

    @pytest.mark.parametrize('code, error_text', getExcelByRow('优惠码错误', 2, 1, 'Store/store.xlsx'))
    @allure.title('pmm购买页面填写空优惠码测试')
    def test_018(self, code, error_text):
        """pmm购买页面填写空优惠码测试"""
        allure.dynamic.tag('优惠码==》{}'.format(code))
        self.driver.click_buy_pmm_button()
        self.driver.switch_pmm_iframe()
        self.driver.buy_addCoupon_step(code)
        self.driver.assert_code_null_text(error_text)

    # @pytest.mark.parametrize('code, error_text', getExcelByRow('优惠码错误', 3, 1, 'Store/store.xlsx'))
    @pytest.mark.skip("未找到过期优惠码")
    @allure.title('pmm购买页面填写过期优惠码测试')
    def test_019(self, code, error_text):
        """pmm购买页面填写空优惠码功能测试"""
        allure.dynamic.tag('优惠码==》{}'.format(code))
        self.driver.click_buy_pmm_button()
        self.driver.switch_pmm_iframe()
        self.driver.buy_addCoupon_step(code)
        self.driver.assert_code_null_text(error_text)

    @pytest.mark.parametrize('code, discount', getExcelAllData('优惠码正确', 'Store/store.xlsx'))
    @allure.title('pmm购买页面填写正确优惠码测试')
    def test_020(self, code, discount):
        """pmm购买页面填写正确优惠码功能测试"""
        allure.dynamic.tag('使用优惠码：{}优惠{}%'.format(code, int(100 * (1 - discount))))
        self.driver.click_buy_pmm_button()
        self.driver.switch_pmm_iframe()
        self.driver.buy_addCoupon_step(code)
        self.driver.assert_after_discount_price(discount)

    @pytest.mark.parametrize('code', getExcelOneCol('优惠码正确', 1, 'Store/store.xlsx'))
    @allure.title('pmm购买页面移除优惠码测试')
    def test_021(self, code):
        """pmm购买页面移除优惠码功能测试"""
        allure.dynamic.tag('移除优惠码')
        self.driver.click_buy_pmm_button()
        self.driver.switch_pmm_iframe()
        self.driver.buy_addCoupon_step(code)
        self.driver.click_delete_coupon()
        self.driver.assert_after_discount_price()

    @allure.title('pmm购买页面取消添加优惠码测试')
    def test_022(self):
        """pmm购买页面取消添加优惠码功能测试"""
        allure.dynamic.tag('取消添加优惠码')
        self.driver.click_buy_pmm_button()
        self.driver.switch_pmm_iframe()
        self.driver.buy_three_step()
        self.driver.click_add_coupon()
        self.driver.cancel_coupon()
        self.driver.assert_after_discount_price()

    @pytest.mark.parametrize('number,name,month,year,pwd,error_text', getExcelAllData('卡片支付', 'Store/store.xlsx'))
    @allure.title('pmm购买页面添加支付卡信息错误测试')
    @allure.severity('critical')
    def test_023(self, number, name, month, year, pwd, error_text):
        """pmm购买页面添加支付卡信息错误功能测试"""
        allure.dynamic.tag('填写支付卡信息')
        self.driver.click_buy_pmm_button()
        self.driver.switch_pmm_iframe()
        self.driver.buy_three_step()
        self.driver.card_to_pay()
        self.driver.send_cardNumber(number)
        self.driver.send_cardName(name)
        self.driver.send_cardMonth(month)
        self.driver.send_cardYear(year)
        self.driver.send_cardPwd(pwd)
        self.driver.submit_card()
        self.driver.assert_card_pay_error_texts(error_text)

    @pytest.mark.parametrize('number,name,month,year,pwd,error_text', getExcelAllData('卡片支付银行异常', 'Store/store.xlsx'))
    @allure.title('pmm购买页面添加支付卡信息银行安全测试')
    def test_024(self, number, name, month, year, pwd, error_text):
        """pmm购买页面添加支付卡信息银行拒绝功能测试"""
        allure.dynamic.tag('填写支付卡信息')
        self.driver.click_buy_pmm_button()
        self.driver.switch_pmm_iframe()
        self.driver.buy_three_step()
        self.driver.card_to_pay()
        self.driver.send_cardNumber(number)
        self.driver.send_cardName(name)
        self.driver.send_cardMonth(month)
        self.driver.send_cardYear(year)
        self.driver.send_cardPwd(pwd)
        self.driver.submit_card()
        self.driver.assert_card_pay_BANK_error_text(error_text)

    @allure.title('pmm购买页面使用其他支付方式测试')
    def test_025(self):
        """pmm购买页面使用其他支付方式功能测试"""
        allure.dynamic.tag('取消原支付方式')
        self.driver.click_buy_pmm_button()
        self.driver.switch_pmm_iframe()
        self.driver.buy_three_step()
        self.driver.card_to_pay()
        self.driver.cancel_pay()
        self.driver.assert_cancel_pay()

    @allure.title('pmm购买页面使用paypal支付测试')
    def test_026(self):
        """pmm购买页面使用paypal支付功能测试"""
        allure.dynamic.tag('paypal支付方式')
        self.driver.click_buy_pmm_button()
        self.driver.switch_pmm_iframe()
        self.driver.buy_three_step()
        self.driver.paypal_to_pay()
        self.driver.assert_goto_paypal()

    @allure.title('pmm购买页面取消paypal支付方式测试')
    def test_027(self):
        """pmm购买页面取消paypal支付方式功能测试"""
        allure.dynamic.tag('取消paypal支付')
        self.driver.click_buy_pmm_button()
        self.driver.switch_pmm_iframe()
        self.driver.buy_three_step()
        self.driver.paypal_to_pay()
        self.driver.cancel_paypal_pay()
        self.driver.assert_cancel_pay()

    @pytest.mark.parametrize('number', ['1', '2', '3', '5', '10', '25'])
    @allure.title('video购买页面填写购买数量测试')
    def test_028(self, number):
        """video购买页面填写购买数量功能测试"""
        allure.dynamic.tag('购买数量为==》{}'.format(number))
        self.driver.click_buy_video_button()
        self.driver.switch_video_iframe()
        self.driver.buy_first_step()
        self.driver.click_num_select()
        self.driver.num_select(number)
        self.driver.assert_price(number)

    @pytest.mark.parametrize('email_data, error_text', getExcelAllData('邮箱错误', 'Store/store.xlsx'))
    @allure.title('video购买页面填写错误格式邮箱测试')
    @allure.severity('normal')
    def test_029(self, email_data, error_text):
        """video购买页面填写错误格式邮箱功能测试"""
        allure.dynamic.tag('邮箱为==》{}'.format(email_data))
        self.driver.click_buy_video_button()
        self.driver.switch_video_iframe()
        self.driver.buy_first_step()
        self.driver.send_email('')
        self.driver.confirm_email()
        self.driver.send_email(email_data)
        self.driver.confirm_email()
        self.driver.assert_email_error_text(error_text)

    @pytest.mark.parametrize('email_data', getExcelOneCol('邮箱正确', 1, 'Store/store.xlsx'))
    @allure.title('video购买页面填写正确格式邮箱测试')
    def test_030(self, email_data):
        """video购买页面填写正确格式邮箱功能测试"""
        allure.dynamic.tag('邮箱为==》{}'.format(email_data))
        self.driver.click_buy_video_button()
        self.driver.switch_video_iframe()
        self.driver.buy_first_step()
        self.driver.send_email(email_data)
        self.driver.confirm_email()
        self.driver.assert_goto_region_page() and self.driver.assert_customer_email(email_data)

    @pytest.mark.parametrize('region, language', getExcelAllData('语言简写', 'Store/store.xlsx'))
    @allure.title('video购买页面填写地区测试')
    def test_031(self, region, language):
        """video购买页面填写地区功能测试"""
        allure.dynamic.tag('地区选择==》{}'.format(language))
        self.driver.click_buy_video_button()
        self.driver.switch_video_iframe()
        self.driver.buy_two_step()
        self.driver.region_select()
        self.driver.region_select_by_value(region)
        self.driver.assert_region_option_text(language)

    @allure.title('video购买页面提交地区测试')
    def test_032(self):
        """video购买页面提交地区功能测试"""
        allure.dynamic.tag('提交地区')
        self.driver.click_buy_video_button()
        self.driver.switch_video_iframe()
        self.driver.buy_three_step()
        self.driver.assert_goto_pay_page()

    @allure.title('video购买页面重新填写邮箱测试')
    def test_033(self):
        """video购买页面重新填写邮箱功能测试"""
        allure.dynamic.tag('更改邮箱')
        self.driver.click_buy_video_button()
        self.driver.switch_video_iframe()
        self.driver.buy_two_step()
        self.driver.click_update_email()
        self.driver.assert_again_send_email()

    @pytest.mark.parametrize('code, error_text', getExcelByRow('优惠码错误', 1, 1, 'Store/store.xlsx'))
    @allure.title('video购买页面填写错误优惠码测试')
    def test_034(self, code, error_text):
        """video购买页面填写错误优惠码功能测试"""
        allure.dynamic.tag('优惠码==》{}'.format(code))
        self.driver.click_buy_video_button()
        self.driver.switch_video_iframe()
        self.driver.buy_addCoupon_step(code)
        self.driver.assert_code_error_text(error_text)

    @pytest.mark.parametrize('code, error_text', getExcelByRow('优惠码错误', 2, 1, 'Store/store.xlsx'))
    @allure.title('video购买页面填写空优惠码测试')
    def test_035(self, code, error_text):
        """video购买页面填写空优惠码测试"""
        allure.dynamic.tag('优惠码==》{}'.format(code))
        self.driver.click_buy_video_button()
        self.driver.switch_video_iframe()
        self.driver.buy_addCoupon_step(code)
        self.driver.assert_code_null_text(error_text)

    # @pytest.mark.parametrize('code, error_text', getExcelByRow('优惠码错误', 3, 1, 'Store/store.xlsx'))
    @pytest.mark.skip("未找到过期优惠码")
    @allure.title('video购买页面填写过期优惠码测试')
    def test_036(self, code, error_text):
        """video购买页面填写空优惠码功能测试"""
        allure.dynamic.tag('优惠码==》{}'.format(code))
        self.driver.click_buy_video_button()
        self.driver.switch_video_iframe()
        self.driver.buy_addCoupon_step(code)
        self.driver.assert_code_null_text(error_text)

    @pytest.mark.parametrize('code, discount', getExcelAllData('优惠码正确', 'Store/store.xlsx'))
    @allure.title('video购买页面填写正确优惠码测试')
    def test_037(self, code, discount):
        """pmm购买页面填写正确优惠码功能测试"""
        allure.dynamic.tag('使用优惠码：{}优惠{}%'.format(code, int(100 * (1 - discount))))
        self.driver.click_buy_video_button()
        self.driver.switch_video_iframe()
        self.driver.buy_addCoupon_step(code)
        self.driver.assert_after_discount_price(discount)

    @pytest.mark.parametrize('code', getExcelOneCol('优惠码正确', 1, 'Store/store.xlsx'))
    @allure.title('video购买页面移除优惠码测试')
    def test_038(self, code):
        """video购买页面移除优惠码功能测试"""
        allure.dynamic.tag('移除优惠码')
        self.driver.click_buy_video_button()
        self.driver.switch_video_iframe()
        self.driver.buy_addCoupon_step(code)
        self.driver.click_delete_coupon()
        self.driver.assert_after_discount_price()

    @allure.title('video购买页面取消添加优惠码测试')
    def test_039(self):
        """video购买页面取消添加优惠码功能测试"""
        allure.dynamic.tag('取消添加优惠码')
        self.driver.click_buy_video_button()
        self.driver.switch_video_iframe()
        self.driver.buy_three_step()
        self.driver.click_add_coupon()
        self.driver.cancel_coupon()
        self.driver.assert_after_discount_price()

    @pytest.mark.parametrize('number,name,month,year,pwd,error_text', getExcelAllData('卡片支付', 'Store/store.xlsx'))
    @allure.title('video购买页面添加支付卡信息错误测试')
    @allure.severity('critical')
    def test_040(self, number, name, month, year, pwd, error_text):
        """video购买页面添加支付卡信息错误功能测试"""
        allure.dynamic.tag('填写支付卡信息')
        self.driver.click_buy_video_button()
        self.driver.switch_video_iframe()
        self.driver.buy_three_step()
        self.driver.card_to_pay()
        self.driver.send_cardNumber(number)
        self.driver.send_cardName(name)
        self.driver.send_cardMonth(month)
        self.driver.send_cardYear(year)
        self.driver.send_cardPwd(pwd)
        self.driver.submit_card()
        self.driver.assert_card_pay_error_texts(error_text)

    @pytest.mark.parametrize('number,name,month,year,pwd,error_text', getExcelAllData('卡片支付银行异常', 'Store/store.xlsx'))
    @allure.title('video购买页面添加支付卡信息银行安全测试')
    def test_041(self, number, name, month, year, pwd, error_text):
        """video购买页面添加支付卡信息银行拒绝功能测试"""
        allure.dynamic.tag('填写支付卡信息')
        self.driver.click_buy_video_button()
        self.driver.switch_video_iframe()
        self.driver.buy_three_step()
        self.driver.card_to_pay()
        self.driver.send_cardNumber(number)
        self.driver.send_cardName(name)
        self.driver.send_cardMonth(month)
        self.driver.send_cardYear(year)
        self.driver.send_cardPwd(pwd)
        self.driver.submit_card()
        self.driver.assert_card_pay_BANK_error_text(error_text)

    @allure.title('video购买页面使用其他支付方式测试')
    def test_042(self):
        """video购买页面使用其他支付方式功能测试"""
        allure.dynamic.tag('取消原支付方式')
        self.driver.click_buy_video_button()
        self.driver.switch_video_iframe()
        self.driver.buy_three_step()
        self.driver.card_to_pay()
        self.driver.cancel_pay()
        self.driver.assert_cancel_pay()

    @allure.title('video购买页面使用paypal支付测试')
    def test_043(self):
        """video购买页面使用paypal支付功能测试"""
        allure.dynamic.tag('paypal支付方式')
        self.driver.click_buy_video_button()
        self.driver.switch_video_iframe()
        self.driver.buy_three_step()
        self.driver.paypal_to_pay()
        self.driver.assert_goto_paypal()

    @allure.title('video购买页面取消paypal支付方式测试')
    def test_044(self):
        """video购买页面取消paypal支付方式功能测试"""
        allure.dynamic.tag('取消paypal支付')
        self.driver.click_buy_video_button()
        self.driver.switch_video_iframe()
        self.driver.buy_three_step()
        self.driver.paypal_to_pay()
        self.driver.cancel_paypal_pay()
        self.driver.assert_cancel_pay()
