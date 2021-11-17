from pytest_project.page_object.support.support_page import SupportPage
from pytest_project.common.readconfig import ini
import pytest, allure
from pytest_project.common.readexcel import getExcelAllData, getExcelOneCol


@allure.feature('Support页面测试')
@allure.story('链接页面内容测试')
@allure.severity('critical')
class TestBody(object):
    @pytest.fixture(scope='function', autouse=True)
    def open_url(self, drivers):
        self.driver = SupportPage(drivers)
        self.driver.get_url(ini.get_url('support'))
        self.driver.click_sale_off_link()

    @allure.title('跳转到sales_faq链接测试')
    @allure.tag('跳转链接')
    def test_001(self):
        """跳转到sales_faq链接功能测试"""
        self.driver.click_sales_faq_link()
        assert self.driver.is_sales_faq()

    @allure.tag('跳转链接')
    @allure.title('跳转到product_fa链接测试')
    def test_002(self):
        """跳转到product_fa链接功能测试"""
        self.driver.click_product_faq_link()
        assert self.driver.is_product_faq()

    @allure.tag('跳转链接')
    @allure.title('跳转到registration_code链接测试')
    def test_003(self):
        """跳转到registration_code链接功能测试"""
        self.driver.click_registration_code_link()
        assert self.driver.is_registration_code()

    @allure.tag('跳转链接')
    @allure.title('跳转到refund_policy链接测试')
    def test_004(self):
        """跳转到refund_policy链接功能测试"""
        self.driver.click_refund_policy_link()
        assert self.driver.is_refund_policy()

    @allure.title('sales展开faq测试')
    @allure.tag('展开faq')
    def test_005(self):
        """sales展开faq功能测试"""
        self.driver.click_sales_faq_link()
        self.driver.click_unfold_faq()
        assert self.driver.return_unfold_item_class()

    @allure.title('sales折叠faq测试')
    @allure.tag('折叠faq')
    def test_006(self):
        """sales折叠faq功能测试"""
        self.driver.click_sales_faq_link()
        self.driver.click_fold_faq()
        assert self.driver.return_fold_item_class()

    @allure.title('product展开faq测试')
    @allure.tag('展开faq')
    def test_007(self):
        """product展开faq功能测试"""
        self.driver.click_product_faq_link()
        self.driver.click_unfold_faq()
        assert self.driver.return_unfold_item_class()

    @allure.title('product折叠faq测试')
    @allure.tag('折叠faq')
    def test_008(self):
        """product折叠faq功能测试"""
        self.driver.click_product_faq_link()
        self.driver.click_fold_faq()
        assert self.driver.return_fold_item_class()

    @pytest.mark.parametrize('search', getExcelOneCol('搜索文章', 1, 'Support/support.xlsx'))
    @allure.title('sales搜索文章测试')
    def test_009(self, search):
        """sales搜索文章功能测试"""
        allure.dynamic.tag('搜索文章，关键字为==》{}'.format(search))
        self.driver.click_sales_faq_link()
        self.driver.search_input(search)
        self.driver.click_search_button()
        assert self.driver.return_succeed_search(search)

    @pytest.mark.parametrize('search', getExcelOneCol('搜索文章', 1, 'Support/support.xlsx'))
    @allure.title('product搜索文章测试')
    def test_010(self, search):
        """product搜索文章功能测试"""
        allure.dynamic.tag('搜索文章，关键字为==》{}'.format(search))
        self.driver.click_product_faq_link()
        self.driver.search_input(search)
        self.driver.click_search_button()
        assert self.driver.return_succeed_search(search)

    @pytest.mark.parametrize('search', getExcelOneCol('搜索不到文章', 1, 'Support/support.xlsx'))
    @allure.title('sales搜索不到文章测试')
    @allure.severity('normal')
    def test_011(self, search):
        """sales搜索不到文章功能测试"""
        allure.dynamic.tag('搜索文章，关键字为==》{}'.format(search))
        self.driver.click_sales_faq_link()
        self.driver.search_input(search)
        self.driver.click_search_button()
        assert self.driver.return_fail_search()

    @pytest.mark.parametrize('search',  getExcelOneCol('搜索不到文章', 1, 'Support/support.xlsx'))
    @allure.title('product搜索不到文章测试')
    @allure.severity('normal')
    def test_012(self, search):
        """product搜索不到文章功能测试"""
        allure.dynamic.tag('搜索文章，关键字为==》{}'.format(search))
        self.driver.click_product_faq_link()
        self.driver.search_input(search)
        self.driver.click_search_button()
        assert self.driver.return_fail_search()

    @allure.title('写邮件链接测试')
    def test_013(self):
        """写邮件链接功能测试"""
        allure.dynamic.tag('写邮件')
        self.driver.click_registration_code_link()
        assert self.driver.return_email_href()

    @allure.title('首页邮件链接测试')
    def test_014(self):
        """首页邮件链接功能测试"""
        allure.dynamic.tag('写邮件')
        assert self.driver.return_support_index_email_href()
