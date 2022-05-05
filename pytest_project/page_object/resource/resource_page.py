import allure

from pytest_project.page.basepage import WebPage
from pytest_project.common.readelement import Element
from pytest_project.utils.times import sleep, compare_date

resource = Element('Resource/resource')


class ReSourcePage(WebPage):
    @allure.step('输入搜索关键字')
    def send_search(self, search):
        self.input_text(resource['input'], search)

    @allure.step('按下搜索键')
    def click_input_button(self):
        self.is_click(resource['input-button'], 2)

    @allure.step('按下回车键进行搜索')
    def submit_search_with_ENTER(self):
        self.Key_enter(resource['input'])
        sleep(2)

    def assert_search_content_succeed(self, search):
        self.allure_assert('判断搜索内容是否准确', ('include', search, self.element_text(resource['source-content']).lower()),
                           ('eq', self.element_text(resource['source-text']), search))

    @allure.step('点击标签栏中的标签')
    def click_topics(self, topics):
        self.is_click(resource.readYaml(f'$.topics.{topics}'))

    def assert_article_topics(self, topics):
        self.allure_assert(f'判断是否成功全以{topics}标签展示',
                           ('eq', set(self.elements_text(resource['article-topics'])), {topics}))

    @allure.step('点击文章标题')
    def goto_article_with_title(self, index):
        title = self.elements_text(resource['article-title'])[index]
        self.click_elements(resource['article-title'], index)
        return title

    def assert_goto_article_with_title(self, article_title):
        self.allure_assert('判断点击文章标题与打开后的文章标题是否相同',
                           ('eq', self.element_text(resource['webpage-article-title']), article_title))

    @allure.step('点击文章图片')
    def goto_article_with_img(self, index):
        title = self.elements_text(resource['article-title'])[index]
        self.click_elements(resource['article-img'], index)
        return title

    def assert_goto_article_with_img(self, article_title):
        self.allure_assert('判断点击文章图片与打开后的文章标题是否相同',
                           ('eq', self.element_text(resource['webpage-article-title']), article_title))

    @allure.step('点击文章标签')
    def click_article_topics(self):
        topic = self.element_text(resource['first-article-topics'])
        self.is_click(resource['first-article-topics'])
        return topic

    def click_page(self, page_num: str):
        with allure.step(f'跳转到内容第{page_num}页'):
            self.scroll_to_loc_is_click(resource.readYaml(f'$.article-page-li-button.{page_num}'))

    def assert_goto_page_with_pagenum(self, page_num: str):
        self.allure_assert('判断页面是否能跳转', ('eq', self.element_text(resource['page-check']), page_num),
                           ('eq', self.get_current_url(), f'https://www.imymac.com/resource/?p={page_num}'))

    @allure.step('点击上一页')
    def click_page_up(self):
        self.is_click(resource['page-up-button'])

    @allure.step('点击下一页')
    def click_page_down(self):
        self.is_click(resource['page-down-button'])

    def click_google_plug_page(self, page_num: str):
        with allure.step(f'跳转到内容第{page_num}页'):
            self.is_click(resource.readYaml(f'$.article-page-li-button.{page_num}'))

    def assert_goto_google_plug_page_with_pagenum(self, page_num: str):
        self.allure_assert('判断页面是否能跳转', ('eq', self.element_text(resource['google-page-check']), page_num))

    @allure.step('点击排序按钮')
    def click_select_sort(self):
        self.is_click(resource.readYaml('$.sort.select-sort'))

    @allure.step('点击相关性排序')
    def sort_by_relevance(self):
        self.is_click(resource.readYaml('$.sort.relevance'))

    @allure.step('点击日期排序')
    def sort_by_date(self):
        self.is_click(resource.readYaml('$.sort.date'), 1)

    @allure.step('关闭隐私弹窗')
    def close_cookie_popup(self):
        self.jsInDriver("document.querySelector('div.box-cookies').className = 'box-cookies'")

    def assert_sort_by_date(self):
        data1 = self.element_text(resource['source-content-data']).split("...")[0].strip()
        data2 = self.element_text(resource['source-two-content-data']).split("...")[0].strip()
        self.allure_assert('判断时间排序是否成功', ('ge', compare_date(data1, data2), 0))

    def assert_no_search(self):
        self.allure_assert('判断Google插件是否弹窗未找到', ('not_eq', self.find_element(resource['no-result']), None))
