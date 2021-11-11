from pytest_project.page.basepage import WebPage
from pytest_project.common.readelement import Element
from pytest_project.common.readexcel import getExcelAllData
import allure
from pytest_project.utils.logger import log

support = Element('Support/support')


class SupportPage(WebPage):
    @allure.step('点击Sales FAQS')
    def click_sales_faq_link(self):
        self.is_click(support['sales-faq'])

    @allure.step('点击Product FAQS')
    def click_product_faq_link(self):
        self.is_click(support['general-faqs'])

    @allure.step('点击Registration Code')
    def click_registration_code_link(self):
        self.is_click(support['retrieve-license'])

    @allure.step('点击Refund Policy')
    def click_refund_policy_link(self):
        self.is_click(support['refund'])

    def is_sales_faq(self):
        """判断是否成功跳转链接"""
        with allure.step('判断是否成功跳转链接'):
            return (self.get_current_url(), self.element_txet(support['faq-handle'])) == \
                   getExcelAllData('主页跳转链接', 'Support/support.xlsx')[0]

    def is_product_faq(self):
        """判断是否成功跳转链接"""
        with allure.step('判断是否成功跳转链接'):
            return (self.get_current_url(), self.element_txet(support['faq-handle'])) == \
                   getExcelAllData('主页跳转链接', 'Support/support.xlsx')[1]

    def is_registration_code(self):
        """判断是否成功跳转链接"""
        with allure.step('判断是否成功跳转链接'):
            return (self.get_current_url(), self.element_txet(support['retrieve-handle'])) \
                   == getExcelAllData('主页跳转链接', 'Support/support.xlsx')[2]

    def is_refund_policy(self):
        """判断是否成功跳转链接"""
        with allure.step('判断是否成功跳转链接'):
            return (self.get_current_url(), self.element_txet(support['refund-handle'])) \
                   == getExcelAllData('主页跳转链接', 'Support/support.xlsx')[3]

    @allure.step('展开第二个faq')
    def click_unfold_faq(self):
        self.is_click(support['faq-item'])

    @allure.step('折叠第二个faq')
    def click_fold_faq(self):
        self.is_click(support['faq-item'])
        self.is_click(support['faq-item'])

    def return_unfold_item_class(self):
        """判断展开后div的class"""
        with allure.step('判断是否展开'):
            return self.getAttribute(support['faq-item-class'], 'class') == 'faqItem faqAnswer-show'

    def return_fold_item_class(self):
        """判断折叠后div的class"""
        with allure.step('判断是否折叠'):
            return self.getAttribute(support['faq-item-class'], 'class') == 'faqItem'

    @allure.step('输入搜索关键字')
    def search_input(self, search):
        self.input_text(support['search-input'], search)

    @allure.step('点击搜索按钮')
    def click_search_button(self):
        self.is_click(support['search-button'])

    def return_succeed_search(self, search):
        """判断搜索结果是否成功"""
        with allure.step('判断搜索结果是否成功'):
            return search in self.element_txet(support['search-content']).lower() and search == self.element_txet(
                support['search'
                        '-text'])

    def return_fail_search(self):
        """判断搜索结果是否失败"""
        with allure.step('判断搜索结果是否失败'):
            return self.find_element(support['no-results']) is not None

    def return_email_href(self):
        with allure.step('判断联系邮箱是否正确'):
            return self.getAttribute(support['send-email-button'], 'href') == 'mailto:support@imymac.com'

    def return_support_index_email_href(self):
        with allure.step('判断联系邮箱是否正确'):
            return self.getAttribute(support['email-class'], 'href') == 'mailto:support@imymac.com'
