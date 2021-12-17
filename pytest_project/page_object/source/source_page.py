import allure

from pytest_project.page.basepage import WebPage
from pytest_project.common.readelement import Element, get_any_key_info, get_values_in_name
from pytest_project.utils.times import sleep

resource = Element('Resource/resource')


class SourcePage(WebPage):
    @allure.step('输入搜索关键字')
    def send_search(self, search):
        self.input_text(resource['input'], search)

    @allure.step('按下搜索键')
    def click_input_button(self):
        self.is_click(resource['input-button'])
        sleep(2)

    @allure.step('按下回车键进行搜索')
    def submit_search_with_ENTER(self):
        self.Key_enter(resource['input'])
        sleep(2)

    def return_search_content_succeed(self, search):
        with allure.step('对内容进行检索'):
            return search in self.element_text(resource['source-content']).lower() and \
                   self.element_text(resource['source-text']) == search

    @allure.step('点击左侧的标签')
    def click_topics(self, topics):
        self.is_click(get_any_key_info(topics, resource.data))

    def return_article_topics(self, topics):
        with allure.step('对标签进行检索'):
            return self.element_text(resource['first-article-topics']) == topics

    @allure.step('点击文章链接')
    def goto_article(self):
        self.is_click(resource['article-link'])

    def return_article_head_title(self, article_title):
        with allure.step('对文章链接与文章标题检索'):
            return article_title == self.element_text(resource['article-title'])

    def click_page(self, button_index: str):
        with allure.step('点击第个{}页码按钮'.format(button_index)):
            self.is_click(get_values_in_name().get_values_in_name(resource.data, button_index)[0])

    def return_click_page_before(self):
        return self.element_text(resource['article-link'])

    def return_click_page_after(self):
        return self.element_text(resource['article-link'])

    def return_page_li_class(self, page_index: str):
        with allure.step('判断页码是否跳转'):
            return self.getAttribute(get_values_in_name().get_values_in_name(resource.data, page_index)[1],
                                     'class') == 'active'

    @allure.step('点击上一页')
    def click_page_up(self):
        self.is_click(resource['article-page-left-shift'])

    @allure.step('点击下一页')
    def click_page_down(self):
        self.is_click(resource['article-page-right-shift'])

    @allure.step('点击文章标签')
    def click_article_topics(self):
        self.is_click(resource['article-topics'])

    def is_click_article_topics(self):
        with allure.step('判断是否列出标签下所有文章'):
            return self.element_text(resource['article-topics']).lower().replace(' ', '-') in self.get_current_url()

    def return_no_search(self):
        return self.find_element(resource['no-result']) is not None