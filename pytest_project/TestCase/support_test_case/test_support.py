from pytest_project.page_object.support.support_page import SupportPage
from pytest_project.common.readconfig import ini
import pytest
import allure


@allure.feature('Support页面测试')
@allure.story('链接页面内容测试')
@allure.severity('critical')
class TestBody(object):
    @pytest.fixture(scope='function', autouse=True)
    def open_url(self, drivers):
        self.driver = SupportPage(drivers)
        self.driver.get_url(ini.get_url('support'))

    @allure.title('跳转到faqs链接测试')
    @allure.tag('跳转faqs页面')
    def test_001(self):
        """跳转到faqs链接功能测试"""
        self.driver.click_faq_link()
        self.driver.assert_goto_faqs()

    @allure.tag('跳转retrieve链接')
    @allure.title('跳转到retrieve页面测试')
    def test_002(self):
        """跳转到retrieve链接功能测试"""
        self.driver.click_retrieve_link()
        self.driver.assert_goto_retrieve()

    @allure.tag('跳转refund')
    @allure.title('跳转到refund页面测试')
    def test_003(self):
        """跳转到refund链接功能测试"""
        self.driver.click_refund_policy_link()
        self.driver.assert_goto_refund()

    @allure.tag('发送邮箱')
    @allure.title('弹出系统自带发送邮件的软件')
    def test_004(self):
        """邮件链接功能测试"""
        self.driver.assert_email_href()
