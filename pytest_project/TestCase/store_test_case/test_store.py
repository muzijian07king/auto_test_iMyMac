import allure
import pytest
from pytest_project.page_object.store.store_page import StorePage
from pytest_project.common.readconfig import ini
from pytest_project.common.readelement import Element, get_values_in_name
from pytest_project.common.readexcel import getExcelAllData, getExcelOneCol, getExcelByRow

store = Element('Store/body')


@allure.feature('Store页面测试')
@allure.story('Store主页内容测试')
@allure.severity('blocker')
class TestBody(object):
    @pytest.fixture(scope='function', autouse=True)
    def open_url(self, drivers):
        self.driver = StorePage(drivers)
        self.driver.get_url(ini.get_url('store'))
        self.driver.click_sale_off_link()

    @pytest.mark.parametrize('buy', get_values_in_name().get_values_in_name(store.data, 'buy-button'))
    @allure.title('点击pmm购买按钮测试')
    def test_001(self, buy):
        """点击pmm购买按钮功能测试"""
        allure.dynamic.tag(buy[1].replace('#', ''))
        self.driver.click_buy(buy)
        assert self.driver.is_buy()

    @allure.severity('critical')
    @allure.title('pmm栏点击更多选项按钮测试')
    def test_002(self):
        """pmm栏点击更多选项按钮功能测试"""
        allure.dynamic.tag('去选择pmm更多套餐')
        self.driver.click_pmm_option()
        assert self.driver.is_option('Select Your PowerMyMac License')

    @allure.severity('critical')
    @allure.title('video栏点击更多选项按钮测试')
    def test_003(self):
        """video栏点击更多选项按钮功能测试"""
        allure.dynamic.tag('去选择video更多套餐')
        self.driver.click_video_option()
        assert self.driver.is_option('Select Your Video Converter License')

    @pytest.mark.parametrize('email_data, error_text', getExcelAllData('邮箱错误', 'Store/store.xlsx'))
    @allure.title('pmm购买页面填写错误格式邮箱测试')
    @allure.severity('normal')
    def test_004(self, email_data, error_text):
        """pmm购买页面填写错误格式邮箱功能测试"""
        allure.dynamic.tag('邮箱为==》{}'.format(email_data))
        self.driver.pmm_buy_first_step()
        self.driver.send_email('')
        self.driver.confirm_email()
        self.driver.send_email(email_data)
        self.driver.confirm_email()
        assert self.driver.return_email_error_text() == error_text

    @pytest.mark.parametrize('email_data', getExcelOneCol('邮箱正确', 1, 'Store/store.xlsx'))
    @allure.title('pmm购买页面填写正确格式邮箱测试')
    def test_005(self, email_data):
        """pmm购买页面填写正确格式邮箱功能测试"""
        allure.dynamic.tag('邮箱为==》{}'.format(email_data))
        self.driver.pmm_buy_first_step()
        self.driver.send_email(email_data)
        self.driver.confirm_email()
        assert self.driver.is_goto_region_page() and self.driver.return_customer_email() == email_data

    @pytest.mark.parametrize('number', ['1', '2', '3', '5', '10', '25'])
    @allure.title('pmm购买页面填写购买数量测试')
    def test_006(self, number):
        """pmm购买页面填写购买数量功能测试"""
        allure.dynamic.tag('购买数量为==》{}'.format(number))
        self.driver.pmm_buy_first_step()
        self.driver.num_select(number)
        assert self.driver.return_pmm_price(number)

    @pytest.mark.parametrize('lg, language', getExcelAllData('语言简写', 'Store/store.xlsx'))
    @allure.title('pmm购买页面填写地区测试')
    def test_007(self, lg, language):
        """pmm购买页面填写地区功能测试"""
        allure.dynamic.tag('地区选择==》{}'.format(language))
        self.driver.pmm_buy_two_step()
        self.driver.region_select(lg)
        assert self.driver.return_region_option_text(language)

    @allure.title('pmm购买页面未填写地区测试')
    def test_008(self):
        """pmm购买页面未填写地区功能测试"""
        allure.dynamic.tag('地区为空提交')
        self.driver.pmm_buy_two_step()
        self.driver.js_disable_into_none()
        self.driver.region_select_by_index(0)
        self.driver.confirm_region()
        assert self.driver.return_region_null_error_text()

    @allure.title('pmm购买页面提交地区测试')
    def test_009(self):
        """pmm购买页面提交地区功能测试"""
        allure.dynamic.tag('进入第四步')
        self.driver.pmm_buy_three_step()
        assert self.driver.return_product_price() is not None

    @allure.title('pmm购买页面重新填写邮箱测试')
    def test_010(self):
        """pmm购买页面重新填写邮箱功能测试"""
        allure.dynamic.tag('更改邮箱')
        self.driver.pmm_buy_two_step()
        self.driver.click_update_email()
        assert self.driver.is_again_send_email()

    @pytest.mark.parametrize('code, error_text', getExcelByRow('优惠码错误', 1, 2, 'Store/store.xlsx'))
    @allure.title('pmm购买页面填写错误优惠码测试')
    def test_011(self, code, error_text):
        """pmm购买页面填写错误优惠码功能测试"""
        allure.dynamic.tag('优惠码==》{}'.format(code))
        self.driver.pmm_buy_addCoupon_step(code)
        assert self.driver.return_code_error_text() == error_text

    @pytest.mark.parametrize('code, error_text', getExcelByRow('优惠码错误', 3, 1, 'Store/store.xlsx'))
    @allure.title('pmm购买页面填写空优惠码测试')
    def test_012(self, code, error_text):
        """pmm购买页面填写空优惠码功能测试"""
        allure.dynamic.tag('优惠码==》{}'.format(code))
        self.driver.pmm_buy_addCoupon_step(code)
        assert self.driver.return_code_null_text() == error_text

    @pytest.mark.parametrize('code, discount', getExcelAllData('优惠码正确', 'Store/store.xlsx'))
    @allure.title('pmm购买页面填写正确优惠码测试')
    def test_013(self, code, discount):
        """pmm购买页面填写正确优惠码功能测试"""
        allure.dynamic.tag('使用优惠码：{}优惠{}%'.format(code, int(100 * (1-discount))))
        self.driver.pmm_buy_addCoupon_step(code)
        assert self.driver.return_pmm_after_discount_price(discount)

    @pytest.mark.parametrize('code', getExcelOneCol('优惠码正确', 1, 'Store/store.xlsx'))
    @allure.title('pmm购买页面移除优惠码测试')
    def test_014(self, code):
        """pmm购买页面移除优惠码功能测试"""
        allure.dynamic.tag('移除优惠码')
        self.driver.pmm_buy_addCoupon_step(code)
        self.driver.click_delete_coupon()
        assert self.driver.return_pmm_after_discount_price()

    @allure.title('pmm购买页面取消添加优惠码测试')
    def test_015(self):
        """pmm购买页面取消添加优惠码功能测试"""
        allure.dynamic.tag('取消添加优惠码')
        self.driver.pmm_buy_three_step()
        self.driver.click_add_coupon()
        self.driver.cancel_coupon()
        assert self.driver.return_product_price() == '9.95'

    @pytest.mark.parametrize('number,name,month,year,pwd,error_text', getExcelAllData('卡片支付', 'Store/store.xlsx'))
    @allure.title('pmm购买页面添加支付卡信息错误测试')
    @allure.severity('critical')
    def test_016(self, number, name, month, year, pwd, error_text):
        """pmm购买页面添加支付卡信息错误功能测试"""
        allure.dynamic.tag('填写支付卡信息')
        self.driver.pmm_buy_three_step()
        self.driver.card_to_pay()
        self.driver.send_cardNumber(number)
        self.driver.send_cardName(name)
        self.driver.send_cardMonth(month)
        self.driver.send_cardYear(year)
        self.driver.send_cardPwd(pwd)
        self.driver.submit_card()
        assert error_text in self.driver.return_card_pay_error_texts()

    @pytest.mark.parametrize('number,name,month,year,pwd,error_text', getExcelAllData('卡片支付银行异常', 'Store/store.xlsx'))
    @allure.title('pmm购买页面添加支付卡信息银行拒绝测试')
    def test_017(self, number, name, month, year, pwd, error_text):
        """pmm购买页面添加支付卡信息银行拒绝功能测试"""
        allure.dynamic.tag('填写支付卡信息')
        self.driver.pmm_buy_three_step()
        self.driver.card_to_pay()
        self.driver.send_cardNumber(number)
        self.driver.send_cardName(name)
        self.driver.send_cardMonth(month)
        self.driver.send_cardYear(year)
        self.driver.send_cardPwd(pwd)
        self.driver.submit_card()
        assert error_text in self.driver.return_card_pay_BANK_error_text()

    @allure.title('pmm购买页面使用其他支付方式测试')
    def test_018(self):
        """pmm购买页面使用其他支付方式功能测试"""
        allure.dynamic.tag('取消原支付方式')
        self.driver.pmm_buy_three_step()
        self.driver.card_to_pay()
        self.driver.cancel_pay()
        assert self.driver.is_cancel_pay()

    @allure.title('pmm购买页面使用paypal支付测试')
    def test_019(self):
        """pmm购买页面使用paypal支付功能测试"""
        allure.dynamic.tag('paypal支付方式')
        self.driver.pmm_buy_three_step()
        self.driver.paypal_to_pay()
        assert self.driver.is_goto_paypal()

    @allure.title('pmm购买页面取消paypal支付方式测试')
    def test_020(self):
        """pmm购买页面取消paypal支付方式功能测试"""
        allure.dynamic.tag('取消paypal支付')
        self.driver.pmm_buy_three_step()
        self.driver.paypal_to_pay()
        self.driver.cancel_paypal_pay()
        assert self.driver.is_cancel_pay()

    @pytest.mark.parametrize('email_data, error_text', getExcelAllData('邮箱错误', 'Store/store.xlsx'))
    @allure.title('video购买页面填写错误格式邮箱测试')
    def test_021(self, email_data, error_text):
        """video购买页面填写错误格式邮箱功能测试"""
        allure.dynamic.tag('邮箱为==》{}'.format(email_data))
        self.driver.video_buy_first_step()
        self.driver.send_email('')
        self.driver.confirm_email()
        self.driver.send_email(email_data)
        self.driver.confirm_email()
        assert self.driver.return_email_error_text() == error_text

    @pytest.mark.parametrize('email_data', getExcelOneCol('邮箱正确', 1, 'Store/store.xlsx'))
    @allure.title('video购买页面填写正确格式邮箱测试')
    def test_022(self, email_data):
        """video购买页面填写正确格式邮箱功能测试"""
        allure.dynamic.tag('邮箱为==》{}'.format(email_data))
        self.driver.video_buy_first_step()
        self.driver.send_email(email_data)
        self.driver.confirm_email()
        assert self.driver.is_goto_region_page() and self.driver.return_customer_email() == email_data

    @pytest.mark.parametrize('number', ['1', '2', '3', '5', '10', '25'])
    @allure.title('video购买页面填写购买数量测试')
    def test_023(self, number):
        """video购买页面填写购买数量功能测试"""
        allure.dynamic.tag('购买数量为==》{}'.format(number))
        self.driver.video_buy_first_step()
        self.driver.num_select(number)
        assert self.driver.return_video_price(number)

    @pytest.mark.parametrize('lg, language', getExcelAllData('语言简写', 'Store/store.xlsx'))
    @allure.title('video购买页面填写地区测试')
    def test_024(self, lg, language):
        """video购买页面填写地区功能测试"""
        allure.dynamic.tag('地区选择==》{}'.format(language))
        self.driver.video_buy_two_step()
        self.driver.region_select(lg)
        assert self.driver.return_region_option_text(language)

    @pytest.mark.skip('设计已修改地区禁止填写为空')
    @allure.title('video购买页面未填写地区测试')
    def test_025(self):
        """video购买页面未填写地区功能测试"""
        allure.dynamic.tag('地区为空提交')
        self.driver.video_buy_two_step()
        self.driver.js_disable_into_none()
        self.driver.region_select_by_index(0)
        self.driver.confirm_region()
        assert self.driver.return_region_null_error_text()

    @allure.title('video购买页面提交地区测试')
    def test_026(self):
        """video购买页面提交地区功能测试"""
        allure.dynamic.tag('进入第四步')
        self.driver.video_buy_three_step()
        assert self.driver.return_product_price() is not None

    @allure.title('video购买页面重新填写邮箱测试')
    def test_027(self):
        """video购买页面重新填写邮箱功能测试"""
        allure.dynamic.tag('更改邮箱')
        self.driver.video_buy_two_step()
        self.driver.click_update_email()
        assert self.driver.is_again_send_email()

    @pytest.mark.parametrize('code, error_text', getExcelByRow('优惠码错误', 1, 2, 'Store/store.xlsx'))
    @allure.title('video购买页面填写错误优惠码测试')
    def test_028(self, code, error_text):
        """video购买页面填写错误优惠码功能测试"""
        allure.dynamic.tag('优惠码==》{}'.format(code))
        self.driver.video_buy_addCoupon_step(code)
        assert self.driver.return_code_error_text() == error_text

    @pytest.mark.parametrize('code, error_text', getExcelByRow('优惠码错误', 3, 1, 'Store/store.xlsx'))
    @allure.title('video购买页面填写空优惠码测试')
    def test_029(self, code, error_text):
        """video购买页面填写空优惠码功能测试"""
        allure.dynamic.tag('优惠码==》{}'.format(code))
        self.driver.video_buy_addCoupon_step(code)
        assert self.driver.return_code_null_text() == error_text

    @pytest.mark.parametrize('code, discount', getExcelAllData('优惠码正确', 'Store/store.xlsx'))
    @allure.title('video购买页面填写正确优惠码测试')
    def test_030(self, code, discount):
        """video购买页面填写正确优惠码功能测试"""
        allure.dynamic.tag('使用优惠码：{}折扣{}%'.format(code, int(100 * discount)))
        self.driver.video_buy_addCoupon_step(code)
        assert self.driver.return_video_after_discount_price(discount)

    @pytest.mark.parametrize('code', getExcelOneCol('优惠码正确', 1, 'Store/store.xlsx'))
    @allure.title('video购买页面移除优惠码测试')
    def test_031(self, code):
        """video购买页面移除优惠码功能测试"""
        allure.dynamic.tag('移除优惠码')
        self.driver.video_buy_addCoupon_step(code)
        self.driver.click_delete_coupon()
        assert self.driver.return_video_after_discount_price()

    @allure.title('video购买页面取消添加优惠码测试')
    def test_032(self):
        """video购买页面取消添加优惠码功能测试"""
        allure.dynamic.tag('取消添加优惠码')
        self.driver.video_buy_three_step()
        self.driver.click_add_coupon()
        self.driver.cancel_coupon()
        assert self.driver.return_video_after_discount_price()

    @pytest.mark.parametrize('number,name,month,year,pwd,error_text', getExcelAllData('卡片支付', 'Store/store.xlsx'))
    @allure.title('video购买页面添加支付卡信息错误测试')
    def test_033(self, number, name, month, year, pwd, error_text):
        """video购买页面添加支付卡信息错误功能测试"""
        allure.dynamic.tag('填写支付卡信息')
        self.driver.video_buy_three_step()
        self.driver.card_to_pay()
        self.driver.send_cardNumber(number)
        self.driver.send_cardName(name)
        self.driver.send_cardMonth(month)
        self.driver.send_cardYear(year)
        self.driver.send_cardPwd(pwd)
        self.driver.submit_card()
        assert error_text in self.driver.return_card_pay_error_texts()

    @pytest.mark.parametrize('number,name,month,year,pwd,error_text', getExcelAllData('卡片支付银行异常', 'Store/store.xlsx'))
    @allure.title('video购买页面添加支付卡信息银行拒绝测试')
    def test_034(self, number, name, month, year, pwd, error_text):
        """video购买页面添加支付卡信息银行拒绝功能测试"""
        allure.dynamic.tag('填写支付卡信息')
        self.driver.video_buy_three_step()
        self.driver.card_to_pay()
        self.driver.send_cardNumber(number)
        self.driver.send_cardName(name)
        self.driver.send_cardMonth(month)
        self.driver.send_cardYear(year)
        self.driver.send_cardPwd(pwd)
        self.driver.submit_card()
        assert error_text in self.driver.return_card_pay_BANK_error_text()

    @allure.title('video购买页面使用其他支付方式测试')
    def test_035(self):
        """video购买页面使用其他支付方式功能测试"""
        allure.dynamic.tag('取消原支付方式')
        self.driver.video_buy_three_step()
        self.driver.card_to_pay()
        self.driver.cancel_pay()
        assert self.driver.is_cancel_pay()

    @allure.title('video购买页面使用paypal支付测试')
    def test_036(self):
        """video购买页面使用paypal支付功能测试"""
        allure.dynamic.tag('paypal支付方式')
        self.driver.video_buy_three_step()
        self.driver.paypal_to_pay()
        assert self.driver.is_goto_paypal()

    @allure.title('video购买页面取消paypal支付方式测试')
    def test_037(self):
        """video购买页面取消paypal支付方式功能测试"""
        allure.dynamic.tag('取消paypal支付')
        self.driver.video_buy_three_step()
        self.driver.paypal_to_pay()
        self.driver.cancel_paypal_pay()
        assert self.driver.is_cancel_pay()
