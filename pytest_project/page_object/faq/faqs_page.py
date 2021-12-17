from pytest_project.page.basepage import WebPage
from pytest_project.common.readelement import Element, get_any_key_info
import allure

from pytest_project.utils.times import sleep

faqs = Element('FAQ/index')


class FAQSPage(WebPage):

    def go_to_faq(self, faq_name):
        with allure.step('点击{}常见问题项'.format(faq_name)):
            self.is_click(get_any_key_info(faq_name, faqs.data))

    def is_go_to_faq_right(self, faq_name):
        with allure.step('判断是否进入对应页面'):
            return faq_name.lower() in self.get_current_url() and \
                   faq_name.replace('-', ' ') in self.element_text(faqs['faq-title'])

    @allure.step('展开第二个faq')
    def click_unfold_faq(self):
        self.is_click(faqs['faq-item'])

    @allure.step('折叠第二个faq')
    def click_fold_faq(self):
        self.is_click(faqs['faq-item'])
        self.is_click(faqs['faq-item'])

    def return_unfold_item_class(self):
        """判断展开后div的class"""
        with allure.step('判断是否成功展开'):
            return self.getAttribute(faqs['faq-item-class'], 'class') == 'faqItem faqAnswer-show'

    def return_fold_item_class(self):
        """判断折叠后div的class"""
        with allure.step('判断是否成功折叠'):
            return self.getAttribute(faqs['faq-item-class'], 'class') == 'faqItem'

    @allure.step('输入搜索关键字')
    def search_input(self, search):
        self.input_text(faqs['search-input'], search)

    @allure.step('点击搜索按钮')
    def click_search_button(self):
        self.is_click(faqs['search-button'])
        sleep(2)

    def return_succeed_search(self, search):
        """判断搜索结果是否成功"""
        with allure.step('判断是否成功搜索'):
            return search in self.element_text(faqs['search-content']).lower() and search == self.element_text(
                faqs['search-text'])

    def return_fail_search(self):
        """判断搜索结果是否失败"""
        with allure.step('判断是否弹出搜索结果为空的提示信息'):
            return self.find_element(faqs['no-results']) is not None
