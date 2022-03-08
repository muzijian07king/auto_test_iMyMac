import allure
import pytest
from pytest_project.page_object.not_found.not_found_page import NotFoundPage
from pytest_project.common.readconfig import ini


@allure.feature('404页面测试')
@allure.story('功能测试')
class TestBody(object):
    @pytest.fixture(scope='function', autouse=True)
    def open_url(self, drivers):
        self.driver = NotFoundPage(drivers)
        self.driver.get_url(ini.get_url('404'))

    @allure.title('跳转首页测试')
    @allure.tag('首页')
    @allure.severity('critical')
    def test_001(self):
        self.driver.goto_home()
        self.driver.assert_goto_home()

    @allure.title('跳转帮助页面测试')
    @allure.tag('帮助')
    @allure.severity('critical')
    def test_002(self):
        self.driver.goto_support()
        self.driver.assert_goto_support()

    @allure.title('跳转购买页面测试')
    @allure.tag('购买')
    @allure.severity('critical')
    def test_003(self):
        self.driver.goto_store()
        self.driver.assert_goto_store()

    @allure.title('跳转博客页面测试')
    @allure.tag('博客')
    @allure.severity('critical')
    def test_004(self):
        self.driver.goto_blog()
        self.driver.assert_goto_blog()
