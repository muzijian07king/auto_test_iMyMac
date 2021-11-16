import allure
import pytest
from pytest_project.page_object.store.buy_page import BuyPage
from pytest_project.common.readconfig import ini
from pytest_project.common.readelement import Element
from pytest_project.common.readexcel import getExcelAllData

store = Element('Store/buy-option')


@allure.severity('blocker')
@allure.feature('Store页面测试')
@allure.story('套餐购买页面内容测试')
class TestBody(object):
    @pytest.fixture(scope='function', autouse=True)
    def open_url(self, drivers):
        self.driver = BuyPage(drivers)
        self.driver.get_url(ini.get_url('store'))
        self.driver.click_sale_off_link()

    @allure.title('购买pmm套餐1支付弹窗测试')
    def test_001(self):
        """购买pmm套餐1支付弹窗功能测试"""
        allure.dynamic.tag('购买套餐1')
        self.driver.goto_pmm_option()
        self.driver.click_buy_1_button()
        assert self.driver.is_goto_buy()

    @allure.title('购买pmm套餐2支付弹窗测试')
    def test_002(self):
        """购买pmm套餐2支付弹窗功能测试"""
        allure.dynamic.tag('购买套餐2')
        self.driver.goto_pmm_option()
        self.driver.click_buy_2_button()
        assert self.driver.is_goto_buy()

    @allure.title('购买pmm套餐3支付弹窗测试')
    def test_003(self):
        """购买pmm套餐3支付弹窗功能测试"""
        allure.dynamic.tag('购买套餐3')
        self.driver.goto_pmm_option()
        self.driver.click_buy_3_button()
        assert self.driver.is_goto_buy()

    @allure.title('购买video套餐1支付弹窗测试')
    def test_004(self):
        """购买video套餐1支付弹窗功能测试"""
        allure.dynamic.tag('购买套餐1')
        self.driver.goto_video_option()
        self.driver.click_buy_1_button()
        assert self.driver.is_goto_buy()

    @allure.title('购买video套餐2支付弹窗测试')
    def test_005(self):
        """购买video套餐2支付弹窗功能测试"""
        allure.dynamic.tag('购买套餐2')
        self.driver.goto_video_option()
        self.driver.click_buy_2_button()
        assert self.driver.is_goto_buy()

    @allure.severity('critical')
    @allure.title('购买video套餐3支付弹窗测试')
    def test_006(self):
        """购买video套餐3支付弹窗功能测试"""
        allure.dynamic.tag('购买套餐1')
        self.driver.goto_video_option()
        self.driver.click_buy_3_button()
        assert self.driver.is_goto_buy()

    @allure.severity('critical')
    @allure.title('pmm套餐价格测试')
    def test_007(self):
        """pmm套餐价格功能测试"""
        allure.dynamic.tag('pmm页面套餐价格')
        self.driver.goto_pmm_option()
        assert self.driver.return_price_in_license() == getExcelAllData('购买pmm套餐', 'Store/store.xlsx')

    @allure.severity('critical')
    @allure.title('video套餐价格测试')
    def test_008(self):
        """video套餐价格功能测试"""
        allure.dynamic.tag('video页面套餐价格')
        self.driver.goto_video_option()
        assert self.driver.return_price_in_license() == getExcelAllData('购买video套餐', 'Store/store.xlsx')

    @allure.title('切换家庭永久套餐测试')
    def test_009(self):
        """切换家庭永久套餐功能测试"""
        allure.dynamic.tag('切换套餐')
        self.driver.goto_pmm_option()
        self.driver.click_pmm_lifetime_license_family()
        assert self.driver.is_buy_family()

    @allure.title('切换个人永久套餐测试')
    def test_010(self):
        """切换个人永久套餐功能测试"""
        allure.dynamic.tag('切换套餐')
        self.driver.goto_pmm_option()
        self.driver.click_pmm_lifetime_license_single()
        assert self.driver.is_buy_single()
