import allure
import pytest

from pytest_project.common.readexcel import getExcelOneCol
from pytest_project.page_object.faq.faqs_page import FAQSPage
from pytest_project.common.readconfig import ini
from pytest_project.common.readelement import Element, get_branch_all_keys

faq = Element('FAQ/index')


@allure.feature('FAQ页面测试')
@allure.story('各个模块常见问题测试')
class TestBody(object):
    @pytest.fixture(scope='function', autouse=True)
    def open_url(self, drivers):
        self.driver = FAQSPage(drivers)
        self.driver.get_url(ini.get_url('faq'))
        self.driver.click_sale_off_link()

    @pytest.mark.parametrize('faq_name', get_branch_all_keys().get_branch_all_keys(faq.data, 'FAQS'))
    @allure.title('进入常见问题页面测试')
    def test_001(self, faq_name):
        allure.dynamic.tag('进入{}的常见问题页面'.format(faq_name))
        self.driver.go_to_faq(faq_name)
        assert self.driver.is_go_to_faq_right(faq_name)

    @allure.title('展开faq测试')
    @pytest.mark.parametrize('faq_name', get_branch_all_keys().get_branch_all_keys(faq.data, 'FAQS'))
    def test_002(self, faq_name):
        """展开faq功能测试"""
        allure.dynamic.tag('展开{}的faq'.format(faq_name))
        self.driver.go_to_faq(faq_name)
        self.driver.click_unfold_faq()
        assert self.driver.return_unfold_item_class()

    @pytest.mark.parametrize('faq_name', get_branch_all_keys().get_branch_all_keys(faq.data, 'FAQS'))
    @allure.title('折叠faq测试')
    def test_003(self, faq_name):
        """sales折叠faq功能测试"""
        self.driver.go_to_faq(faq_name)
        self.driver.click_fold_faq()
        assert self.driver.return_fold_item_class()

    @pytest.mark.parametrize('faq_name', get_branch_all_keys().get_branch_all_keys(faq.data, 'FAQS'))
    @pytest.mark.parametrize('search', getExcelOneCol('搜索文章', 1, 'Support/support.xlsx'))
    @allure.title('搜索文章测试')
    @allure.severity('critical')
    def test_004(self, faq_name, search):
        """product搜索文章功能测试"""
        allure.dynamic.tag('搜索文章，关键字为==》{}'.format(search))
        self.driver.go_to_faq(faq_name)
        self.driver.search_input(search)
        self.driver.click_search_button()
        assert self.driver.return_succeed_search(search)

    @pytest.mark.parametrize('faq_name', get_branch_all_keys().get_branch_all_keys(faq.data, 'FAQS'))
    @pytest.mark.parametrize('search', getExcelOneCol('搜索不到文章', 1, 'Support/support.xlsx'))
    @allure.title('搜索不到文章测试')
    @allure.severity('minor')
    def test_005(self, faq_name, search):
        """搜索不到文章功能测试"""
        allure.dynamic.tag('搜索文章，关键字为==》{}'.format(search))
        self.driver.go_to_faq(faq_name)
        self.driver.search_input(search)
        self.driver.click_search_button()
        assert self.driver.return_fail_search()
