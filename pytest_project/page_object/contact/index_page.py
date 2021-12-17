from pytest_project.page.basepage import WebPage
from pytest_project.common.readelement import Element, get_any_key_info
import allure
contact = Element('Contact/contact')


class ContactPage(WebPage):
    def get_contact_text(self, title):
        with allure.step('获取{}下的描述'.format(title)):
            return self.element_text(get_any_key_info(title, contact.data))

    @allure.step('判断发送邮箱链接是否正确')
    def get_send_email(self):
        return self.getAttribute(contact['email-link'], 'href') == 'mailto:support@imymac.com'
