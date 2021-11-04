from pytest_project.page.basepage import WebPage
from pytest_project.common.readelement import Element, get_any_key_info
import allure
policy = Element('Protocol/policy')


class ProtocolPage(WebPage):
    def goto_protocol(self, name):
        with allure.step('打开{}页面'.format(name)):
            self.scroll_to_loc(policy['footer'])
            self.is_click(get_any_key_info(name, policy.data))

    def if_title(self, title):
        with allure.step('判断小标题'):
            return self.elements_text(get_any_key_info('title-l', policy.data)) == title

    def if_headline(self, title):
        with allure.step('判断大标题'):
            return self.element_txet(get_any_key_info('title-h1', policy.data)) == title

    def if_email_in_context(self):
        with allure.step('文章内容判断邮箱链接'):
            return 'mailto:support@imymac.com' in set(self.getAttributes(get_any_key_info
                                                                         ('email', policy.data), 'href'))


