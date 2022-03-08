from pytest_project.page.basepage import WebPage
import allure
from pytest_project.common.readelement import Element, get_any_key_info

discount = Element('Discount/discount')


class DiscountPage(WebPage):
    def assert_step_context(self, step, context):
        result = self.element_text(discount.readYaml(f'$.step-context.{step}')) == context
        self.allure_assert_step('判断步骤文案是否正确', result)
        assert result

    def assert_step_email(self):
        result = self.getAttribute(discount.readYaml('$.step-context.email'), 'href') == 'mailto:support@imymac.com'
        self.allure_assert_step('判断步骤一中邮箱是否正确', result)
        assert result

    def assert_email(self):
        result = self.getAttribute(discount.readYaml('$.email'), 'href') == 'mailto:support@imymac.com'
        self.allure_assert_step('判断底部邮箱是否正确', result)
        assert result

    def assert_discount_email(self, emails: list):
        self.scroll_to_loc(discount['discount-email'])
        result = self.elements_text(discount['discount-email']) == emails
        self.allure_assert_step('判断邮箱是否正确', result)
        assert result
