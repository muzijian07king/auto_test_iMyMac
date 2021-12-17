from pytest_project.page.basepage import WebPage
import allure
from pytest_project.common.readelement import Element, get_any_key_info

discount = Element('Discount/discount')


class DiscountPage(WebPage):
    def step_if_ture(self, step, context):
        with allure.step('判断步骤文案是否正确'):
            return self.element_text(get_any_key_info(step, discount.data)) == context

    @allure.step('点击购买链接')
    def click_store_link(self):
        self.is_click(discount['store'])

    def if_goto_store(self):
        with allure.step('判断是否跳转store'):
            return self.get_current_url() == 'https://www.imymac.com/store/'

    @allure.step('输入EDU邮箱')
    def input_EDU_email(self, email):
        self.input_text(discount['send-email'], email)

    @allure.step('提交邮箱')
    def submit_email(self):
        self.is_click(discount['submit'])

    def submit_feedback(self, feedback):
        self.element_if_display(discount['submit-feedback'])
        with allure.step('判断反馈信息是否正确'):
            return self.element_text(discount['submit-feedback']) == feedback

    def if_goto_send_email(self):
        with allure.step('判断是否去写邮件'):
            return self.getAttribute(discount['email'], 'href') == 'mailto:support@imymac.com'

    @allure.step('搜索邮箱')
    def search_email(self, search):
        self.input_text(discount['search'], search)

    @allure.step('提交搜索')
    def click_search_button(self):
        self.is_click(discount['search-button'])

    def discount_email(self, email):
        with allure.step('判断优惠邮箱'):
            return self.elements_text(discount['discount-email']) == email

