import allure
import pytest
from pytest_project.common.readconfig import ini
from pytest_project.page_object.retrieven.register_page import RegisterPage


@allure.feature('找回用户页面测试')
@allure.severity('critical')
class TestBody(object):

    @pytest.fixture(scope='function', autouse=True)
    def open_url(self, drivers):
        self.driver = RegisterPage(drivers)
        self.driver.get_url(ini.get_url('retrieve'))

    @allure.title('跳转login页面')
    @allure.tag('login页面')
    @allure.story('主页测试')
    @allure.severity('blocker')
    def test_001(self):
        self.driver.goto_login()
        self.driver.assert_goto_login()

    @allure.title('跳转register页面')
    @allure.tag('register页面')
    @allure.story('主页测试')
    @allure.severity('blocker')
    def test_002(self):
        self.driver.goto_register()
        self.driver.assert_goto_register()

    @allure.title('邮箱链接测试')
    @allure.tag('邮箱')
    @allure.story('主页测试')
    @allure.severity('blocker')
    def test_003(self):
        self.driver.assert_email()
