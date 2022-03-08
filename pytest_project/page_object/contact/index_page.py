from pytest_project.page.basepage import WebPage
from pytest_project.common.readelement import Element
import allure
contact = Element('Contact/contact')


class ContactPage(WebPage):
    def assert_contact_text(self, title, desc):
        result = self.element_text(contact[title]) == desc
        self.allure_assert_step(f'判断{title}下的描述是否一致', result)
        assert result

    @allure.step('判断发送邮箱链接是否正确')
    def assert_email(self):
        assert self.getAttribute(contact['email-link'], 'href') == 'mailto:support@imymac.com'
