import allure
import pytest
from pytest_project.common.readconfig import ini
from pytest_project.config.conf import cm
from pytest_project.page_object.source.source_page import SourcePage
from pytest_project.common.readexcel import getExcelOneCol


@allure.feature('文章搜索页面测试')
@allure.story('文章搜索页面功能测试')
@allure.severity('critical')
class TestBody(object):
    @pytest.fixture(scope='function', autouse=True)
    def open_url(self, drivers):
        self.driver = SourcePage(drivers)
        self.driver.get_url(ini.get_url('resource'))
        self.driver.click_sale_off_link()

    @pytest.mark.parametrize('search', getExcelOneCol('搜索文章', 1, 'Resource/resource.xlsx'))
    @pytest.mark.skipif(cm.VPN_Switch, reason='阿里云没有VPN')
    @allure.title('搜索文章测试')
    def test_001(self, search):
        """搜索文章功能测试"""
        allure.dynamic.tag('搜索文章==》{}'.format(search))
        self.driver.send_search(search)
        self.driver.click_input_button()
        assert self.driver.return_search_content_succeed(search)

    @pytest.mark.parametrize('search', getExcelOneCol('搜索文章', 1, 'Resource/resource.xlsx'))
    @allure.title('搜索文章回车测试')
    @pytest.mark.skipif(cm.VPN_Switch, reason='阿里云没有VPN')
    @allure.severity('minor')
    def test_002(self, search):
        """搜索文章回车功能测试"""
        allure.dynamic.tag('搜索文章==》{}'.format(search))
        allure.dynamic.severity('normal')
        self.driver.send_search(search)
        self.driver.submit_search_with_ENTER()
        assert self.driver.return_search_content_succeed(search)

    @pytest.mark.parametrize('topics', getExcelOneCol('文章标签', 1, 'Resource/resource.xlsx'))
    @allure.title('标签栏测试')
    def test_003(self, topics):
        """标签栏功能测试"""
        allure.dynamic.tag('点击标签==》{}'.format(topics))
        self.driver.click_topics(topics)
        assert self.driver.return_article_topics(topics)

    @allure.title('跳转文章测试')
    def test_004(self):
        """跳转文章功能测试"""
        allure.dynamic.tag('跳转文章')
        allure.dynamic.severity('blocker')
        article_title = self.driver.return_click_page_before()
        self.driver.goto_article()
        assert self.driver.return_article_head_title(article_title)

    @allure.title('点击文章标签测试')
    def test_005(self):
        """点击文章标签"""
        allure.dynamic.tag('文章标签按钮')
        self.driver.click_article_topics()
        assert self.driver.is_click_article_topics()

    @pytest.mark.parametrize('index', list(str(x) for x in range(2, 3)))
    @allure.title('切换页码测试')
    def test_006(self, index):
        allure.dynamic.tag('切换页码=={}'.format(index))
        before = self.driver.return_click_page_before()
        self.driver.click_page(index)
        assert self.driver.return_page_li_class(index) and before != self.driver.return_click_page_after()

    @pytest.mark.parametrize('index', list(str(x) for x in range(4, 6)))
    @allure.title('切换页码测试')
    def test_007(self, index):
        allure.dynamic.tag('切换页码=={}'.format(index))
        before = self.driver.return_click_page_before()
        self.driver.click_page(index)
        assert self.driver.return_page_li_class('3') and before != self.driver.return_click_page_after()

    @pytest.mark.skip('翻页功能bug')
    @allure.title('下一页测试')
    def test_008(self):
        allure.dynamic.tag('下一页')
        self.driver.click_page_down()
        assert self.driver.return_page_li_class('2')

    @allure.title('上一页测试')
    def test_009(self):
        allure.dynamic.tag('上一页')
        self.driver.click_page_up()
        assert self.driver.return_page_li_class('1')

    @pytest.mark.parametrize('key', getExcelOneCol('搜索不到文章', 1, 'Resource/resource.xlsx'))
    @allure.title('搜索不到文章测试')
    @pytest.mark.skipif(cm.VPN_Switch, reason='阿里云没有VPN')
    @allure.severity('minor')
    def test_010(self, key):
        allure.dynamic.tag('输入关键字')
        self.driver.send_search(key)
        self.driver.click_input_button()
        assert self.driver.return_no_search()