import allure
import pytest
from pytest_project.page_object.store.store_pmm_option_page import OptionPage
from pytest_project.common.readconfig import ini


@allure.feature('Store测试')
@allure.story('PMM套餐测试')
@allure.severity('blocker')
class TestBody(object):
    @pytest.fixture(scope='function', autouse=True)
    def open_url(self, drivers):
        self.driver = OptionPage(drivers)
        self.driver.get_url(ini.get_url('pmm-store-option'))

    @allure.severity('critical')
    @allure.title('测试产品一个月页面原价')
    @allure.tag('原价')
    def test_001(self):
        self.driver.assert_month_original_price()

    @allure.severity('critical')
    @allure.title('测试产品一个月页面现价')
    @allure.tag('现价')
    def test_002(self):
        self.driver.assert_month_now_price()

    @allure.severity('critical')
    @allure.title('测试产品一个月页面优惠价')
    @allure.tag('优惠价')
    def test_003(self):
        self.driver.assert_month_discounts_price()

    @allure.severity('critical')
    @allure.title('测试产品一年一台页面原价')
    @allure.tag('原价')
    def test_004(self):
        self.driver.switch_to_year_one_button()
        self.driver.assert_year_one_original_price()

    @allure.severity('critical')
    @allure.title('测试产品一年一台页面现价')
    @allure.tag('现价')
    def test_005(self):
        self.driver.switch_to_year_one_button()
        self.driver.assert_year_one_now_price()

    @allure.severity('critical')
    @allure.title('测试产品一年一台页面优惠价')
    @allure.tag('优惠价')
    def test_006(self):
        self.driver.switch_to_year_one_button()
        self.driver.assert_year_one_discounts_price()

    @allure.severity('critical')
    @allure.title('测试产品一年两台页面原价')
    @allure.tag('原价')
    def test_007(self):
        self.driver.switch_to_year_two_button()
        self.driver.assert_year_two_original_price()

    @allure.severity('critical')
    @allure.title('测试产品一年两台页面现价')
    @allure.tag('现价')
    def test_008(self):
        self.driver.switch_to_year_two_button()
        self.driver.assert_year_two_now_price()

    @allure.severity('critical')
    @allure.title('测试产品一年两台页面优惠价')
    @allure.tag('优惠价')
    def test_009(self):
        self.driver.switch_to_year_two_button()
        self.driver.assert_year_two_discounts_price()

    @allure.severity('critical')
    @allure.title('测试产品一年五台页面原价')
    @allure.tag('原价')
    def test_010(self):
        self.driver.switch_to_year_five_button()
        self.driver.assert_year_five_original_price()

    @allure.severity('critical')
    @allure.title('测试产品一年五台页面现价')
    @allure.tag('现价')
    def test_011(self):
        self.driver.switch_to_year_five_button()
        self.driver.assert_year_five_now_price()

    @allure.severity('critical')
    @allure.title('测试产品一年五台页面优惠价')
    @allure.tag('优惠价')
    def test_012(self):
        self.driver.switch_to_year_five_button()
        self.driver.assert_year_five_discounts_price()

    @allure.severity('critical')
    @allure.title('测试产品永久一台页面原价')
    @allure.tag('原价')
    def test_013(self):
        self.driver.switch_to_lifetime_one_button()
        self.driver.assert_lifetime_one_original_price()

    @allure.severity('critical')
    @allure.title('测试产品永久一台页面现价')
    @allure.tag('现价')
    def test_014(self):
        self.driver.switch_to_lifetime_one_button()
        self.driver.assert_lifetime_one_now_price()

    @allure.severity('critical')
    @allure.title('测试产品永久一台页面优惠价')
    @allure.tag('优惠价')
    def test_015(self):
        self.driver.switch_to_lifetime_one_button()
        self.driver.assert_lifetime_one_discounts_price()

    @allure.severity('critical')
    @allure.title('测试产品永久两台页面原价')
    @allure.tag('原价')
    def test_016(self):
        self.driver.switch_to_lifetime_two_button()
        self.driver.assert_lifetime_two_original_price()

    @allure.severity('critical')
    @allure.title('测试产品永久两台页面现价')
    @allure.tag('现价')
    def test_017(self):
        self.driver.switch_to_lifetime_two_button()
        self.driver.assert_lifetime_two_now_price()

    @allure.severity('critical')
    @allure.title('测试产品永久两台页面优惠价')
    @allure.tag('优惠价')
    def test_018(self):
        self.driver.switch_to_lifetime_two_button()
        self.driver.assert_lifetime_two_discounts_price()

    @allure.severity('critical')
    @allure.title('测试产品永久五台页面原价')
    @allure.tag('原价')
    def test_019(self):
        self.driver.switch_to_lifetime_five_button()
        self.driver.assert_lifetime_five_original_price()

    @allure.severity('critical')
    @allure.title('测试产品永久五台页面现价')
    @allure.tag('现价')
    def test_020(self):
        self.driver.switch_to_lifetime_five_button()
        self.driver.assert_lifetime_five_now_price()

    @allure.severity('critical')
    @allure.title('测试产品永久五台页面优惠价')
    @allure.tag('优惠价')
    def test_021(self):
        self.driver.switch_to_lifetime_five_button()
        self.driver.assert_lifetime_five_discounts_price()

    @allure.title('测试购买一个月pay支付弹窗信息')
    @allure.tag('一个月')
    def test_022(self):
        self.driver.click_buy_month_button()
        self.driver.switch_to_month_pay()
        self.driver.assert_month_pay()

    @allure.title('测试购买一年一台pay支付弹窗信息')
    @allure.tag('一年一台')
    def test_023(self):
        self.driver.click_buy_year_one_button()
        self.driver.switch_to_year_one_pay()
        self.driver.assert_year_one_pay()

    @allure.title('测试购买一年两台pay支付弹窗信息')
    @allure.tag('一年两台')
    def test_024(self):
        self.driver.switch_to_year_two_button()
        self.driver.click_buy_year_two_button()
        self.driver.switch_to_year_two_pay()
        self.driver.assert_year_two_pay()

    @allure.title('测试购买一年五台pay支付弹窗信息')
    @allure.tag('一年五台')
    def test_025(self):
        self.driver.switch_to_year_five_button()
        self.driver.click_buy_year_five_button()
        self.driver.switch_to_year_five_pay()
        self.driver.assert_year_five_pay()

    @allure.title('测试购买永久一台pay支付弹窗信息')
    @allure.tag('永久一台')
    def test_026(self):
        self.driver.switch_to_lifetime_one_button()
        self.driver.click_buy_lifetime_one_button()
        self.driver.switch_to_lifetime_one_pay()
        self.driver.assert_lifetime_one_pay()

    @allure.title('测试购买永久两台pay支付弹窗信息')
    @allure.tag('永久两台')
    def test_027(self):
        self.driver.switch_to_lifetime_two_button()
        self.driver.click_buy_lifetime_two_button()
        self.driver.switch_to_lifetime_two_pay()
        self.driver.assert_lifetime_two_pay()

    @allure.title('测试购买永久五台pay支付弹窗信息')
    @allure.tag('永久五台')
    def test_028(self):
        self.driver.switch_to_lifetime_five_button()
        self.driver.click_buy_lifetime_five_button()
        self.driver.switch_to_lifetime_five_pay()
        self.driver.assert_lifetime_five_pay()

    @allure.title('测试展开所有问题')
    @allure.tag('faqs')
    def test_029(self):
        self.driver.click_unfold_faqs_button()
        self.driver.assert_faqs_fold()

    @allure.title('测试折叠所有问题')
    @allure.tag('faqs')
    def test_030(self):
        self.driver.click_unfold_faqs_button()
        self.driver.click_fold_faqs_button()
        self.driver.assert_faqs_unfold()
