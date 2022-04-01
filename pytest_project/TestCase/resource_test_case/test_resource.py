import random

import allure
import pytest
from pytest_project.common.readconfig import ini
from pytest_project.config.conf import cm
from pytest_project.page_object.resource.resource_page import ReSourcePage
from pytest_project.common.readexcel import getExcelOneCol


@allure.feature('文章搜索页面测试')
@allure.story('文章搜索页面功能测试')
@allure.severity('blocker')
class TestBody(object):
    @pytest.fixture(scope='function', autouse=True)
    def open_url(self, drivers):
        self.driver = ReSourcePage(drivers)
        self.driver.get_url(ini.get_url('resource'))
        self.driver.close_cookie_popup()

    @pytest.mark.parametrize('search', getExcelOneCol('搜索文章', 1, 'Resource/resource.xlsx'))
    @pytest.mark.skipif(cm.VPN_Switch, reason='阿里云没有VPN')
    @allure.title('搜索文章测试')
    def test_001(self, search):
        """搜索文章功能测试"""
        allure.dynamic.tag('搜索文章==》{}'.format(search))
        self.driver.send_search(search)
        self.driver.click_input_button()
        self.driver.assert_search_content_succeed(search)

    @pytest.mark.parametrize('search', getExcelOneCol('搜索文章', 1, 'Resource/resource.xlsx'))
    @allure.title('搜索文章回车测试')
    @pytest.mark.skipif(cm.VPN_Switch, reason='阿里云没有VPN')
    @allure.severity('normal')
    def test_002(self, search):
        """搜索文章回车功能测试"""
        allure.dynamic.tag('搜索文章==》{}'.format(search))
        allure.dynamic.severity('normal')
        self.driver.send_search(search)
        self.driver.submit_search_with_ENTER()
        self.driver.assert_search_content_succeed(search)

    @pytest.mark.parametrize('topics', getExcelOneCol('文章标签', 1, 'Resource/resource.xlsx'))
    @allure.title('标签栏测试')
    def test_003(self, topics):
        """标签栏功能测试"""
        allure.dynamic.tag('点击标签==》{}'.format(topics))
        self.driver.click_topics(topics)
        self.driver.assert_article_topics(topics)

    @allure.title('文章标题跳转文章测试')
    @pytest.mark.parametrize('index', list(range(9)))
    def test_004(self, index):
        """跳转文章功能测试"""
        allure.dynamic.tag(f'第{index + 1}文章标题')
        article_title = self.driver.goto_article_with_title(index)
        self.driver.assert_goto_article_with_title(article_title)

    @allure.title('文章图片跳转文章测试')
    @pytest.mark.parametrize('index', list(range(9)))
    def test_005(self, index):
        """跳转文章功能测试"""
        allure.dynamic.tag(f'第{index + 1}篇文章图片')
        article_title = self.driver.goto_article_with_img(index)
        self.driver.assert_goto_article_with_img(article_title)

    @allure.title('点击文章标签测试')
    def test_006(self):
        """点击文章标签"""
        topic = self.driver.click_article_topics()
        allure.dynamic.tag(f'{topic}标签')
        self.driver.assert_article_topics(topic)

    @pytest.mark.parametrize('index', list(range(1, 10)))
    @allure.title('切换页码测试')
    def test_007(self, index):
        allure.dynamic.tag('切换页码=={}'.format(index))
        self.driver.click_page(str(index))
        self.driver.assert_goto_page_with_pagenum(str(index))

    @allure.title('点击上一页功能测试')
    @allure.tag('上一页')
    def test_008(self):
        random_number = random.randint(2, 9)
        self.driver.click_page(str(random_number))
        self.driver.close_cookie_popup()
        self.driver.click_page_up()
        self.driver.assert_goto_page_with_pagenum(str(random_number - 1))

    @allure.title('点击下一页功能测试')
    @allure.tag('下一页')
    def test_009(self):
        random_number = random.randint(1, 9)
        self.driver.click_page(str(random_number))
        self.driver.close_cookie_popup()
        self.driver.click_page_down()
        self.driver.assert_goto_page_with_pagenum(str(random_number + 1))

    @pytest.mark.parametrize('key', getExcelOneCol('搜索不到文章', 1, 'Resource/resource.xlsx'))
    @allure.title('搜索不到文章测试')
    @pytest.mark.skipif(cm.VPN_Switch, reason='阿里云没有VPN')
    @allure.severity('minor')
    def test_010(self, key):
        allure.dynamic.tag('输入关键字')
        self.driver.send_search(key)
        self.driver.click_input_button()
        self.driver.assert_no_search()

    @allure.title('Google相关性排序测试')
    @allure.tag('相关性')
    def test_011(self):
        self.driver.send_search('java')
        self.driver.click_input_button()
        self.driver.click_select_sort()
        self.driver.sort_by_relevance()
        self.driver.assert_search_content_succeed('c')

    @pytest.mark.timeout(30)
    @allure.title('Google时间排序测试')
    @allure.tag('时间')
    @pytest.mark.flaky(reruns=0)
    def test_012(self):
        self.driver.send_search('c')
        self.driver.click_input_button()
        self.driver.close_cookie_popup()
        self.driver.click_select_sort()
        self.driver.sort_by_date()
        self.driver.assert_sort_by_date()

