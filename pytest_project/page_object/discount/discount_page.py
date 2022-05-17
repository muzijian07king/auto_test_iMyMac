from pytest_project.page.basepage import WebPage
from pytest_project.common.readelement import Element

discount = Element('Discount/discount')


class DiscountPage(WebPage):
    def assert_step_context(self, step, context):
        self.allure_assert('判断步骤文案是否正确',
                           ('eq', self.element_text(discount.readYaml(f'$.step-context.{step}')), context))

    def assert_step_email(self):
        self.allure_assert('判断步骤一中邮箱是否正确', (
            'eq', self.getAttribute(discount.readYaml('$.step-context.email'), 'href'), 'mailto:support@imymac.com'))

    def assert_email(self):
        self.allure_assert("判断底部邮箱是否正确",
                           ('eq', self.getAttribute(discount.readYaml('$.email'), 'href'), 'mailto:support@imymac.com'))

    def assert_discount_email(self, emails: list):
        self.scroll_to_loc(discount['discount-email'])
        self.allure_assert('判断邮箱是否正确', ('eq', self.elements_text(discount['discount-email']), emails))
