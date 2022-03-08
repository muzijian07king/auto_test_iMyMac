from pytest_project.page.basepage import WebPage
from pytest_project.common.readelement import Element
from pytest_project.common.readexcel import getExcelAllData
import allure
from pytest_project.utils.times import sleep

support = Element('Support/support')


class SupportPage(WebPage):
    @allure.step('点击FAQS')
    def click_faq_link(self):
        self.is_click(support['faqs'])

    @allure.step('点击Retrieve License')
    def click_retrieve_link(self):
        self.is_click(support['retrieve'])

    @allure.step('点击Refund Policy')
    def click_refund_policy_link(self):
        self.is_click(support['refund'])

    def assert_goto_faqs(self):
        result = self.get_current_url() == 'https://www.imymac.com/faqs/'
        self.allure_assert_step('判断成功跳转到faq页面', result)
        assert result

    def assert_goto_retrieve(self):
        result = self.get_current_url() == 'https://www.imymac.com/retrieve-license.html'
        self.allure_assert_step('判断成功跳转到retrieve页面', result)
        assert result

    def assert_goto_refund(self):
        result = self.get_current_url() == 'https://www.imymac.com/refund.html'
        self.allure_assert_step('判断成功跳转到refund页面', result)
        assert result

    def assert_email_href(self):
        result = self.getAttribute(support['email'], 'href') == 'mailto:support@imymac.com'
        self.allure_assert_step('判断联系邮箱是否正确', result)
        assert result
