import allure
import pytest
from pytest_project.common.readconfig import ini
from pytest_project.page_object.retrieven.login_page import LoginPage
from pytest_project.common.readexcel import getExcelAllData, getValueByIndex
from pytest_project.common.readelement import Element


@allure.feature('用户系统测试')
@allure.story('登录页面功能测试')
@allure.severity('critical')
class TestBody(object):

    @pytest.fixture(scope='function', autouse=True)
    def open_url(self, drivers):
        self.driver = LoginPage(drivers)
        self.driver.get_url(ini.get_url('login'))

    @pytest.fixture(scope='function')
    def switch_language(self):
        self.driver.click_unfold_language()
        self.driver.click_language('en')

    @pytest.fixture(scope='function')
    def clear_cookie(self):
        self.driver.delete_all_cookie()
        self.driver.refresh()

    @pytest.fixture(scope='function')
    def update_cookie(self):
        yield
        cookie = self.driver.get_cookie(Element('User/cookie').readYaml('$.name', 1))
        self.driver.update_member_imymac_cookie(cookie)

    @allure.title('登录成功测试')
    @allure.tag('登录成功')
    @allure.severity('blocker')
    def test_001(self, switch_language):
        self.driver.input_email(getValueByIndex(2, 2, '注册成功', 'Admin/register.xlsx'))
        self.driver.input_password(getValueByIndex(3, 2, '注册成功', 'Admin/register.xlsx'))
        self.driver.click_login()
        self.driver.assert_login_succeed(getValueByIndex(1, 2, '注册成功', 'Admin/register.xlsx'))

    @allure.title('勾选记住我功能测试')
    @allure.tag('勾选记住我')
    @pytest.mark.flaky(reruns=0)
    def test_002(self, switch_language, clear_cookie, update_cookie):
        email = getValueByIndex(2, 2, '注册成功', 'Admin/register.xlsx')
        password = getValueByIndex(3, 2, '注册成功', 'Admin/register.xlsx')
        self.driver.input_email(email)
        self.driver.input_password(password)
        self.driver.check_remember()
        self.driver.click_login()
        self.driver.assert_remember_function(email)

    @allure.title('登录失败测试')
    @allure.severity('critical')
    @pytest.mark.parametrize('email,pwd,cause', getExcelAllData('登录失败', 'Admin/login.xlsx'))
    def test_003(self, email, pwd, cause, switch_language, clear_cookie):
        if pwd in [' 123456789', '123456789 ']:
            pytest.xfail('会自动将首尾的空格去除，待修复')
        allure.dynamic.tag(cause)
        self.driver.input_email(email)
        self.driver.input_password(pwd)
        self.driver.click_login()
        self.driver.assert_error_popup()

    @allure.title('跳转注册页面测试')
    @allure.tag('跳转注册页面')
    @allure.severity('blocker')
    def test_004(self):
        self.driver.click_register()
        self.driver.assert_goto_register()

    @allure.title('跳转找回密码页面测试')
    @allure.tag('跳转找回密码页面')
    @allure.severity('blocker')
    def test_005(self):
        self.driver.goto_forgot()
        self.driver.assert_goto_forgot()

    @allure.title('勾选记住我按钮测试')
    @allure.tag('勾选记住我')
    @allure.severity('normal')
    def test_006(self):
        self.driver.check_remember()
        self.driver.assert_check_remember()

    @allure.title('取消勾选记住我功能测试')
    @allure.tag('取消勾选记住我')
    @allure.severity('normal')
    def test_007(self):
        self.driver.cancel_check_remember()
        self.driver.assert_cancel_check_remember()

    @allure.title('展开语言选择框测试')
    @allure.tag('展开语言')
    @allure.severity('blocker')
    def test_008(self):
        self.driver.click_unfold_language()
        self.driver.assert_unfold_language()

    @allure.title('折叠语言选择框测试')
    @allure.tag('折叠语言')
    @allure.severity('blocker')
    def test_009(self):
        self.driver.click_fold_language()
        self.driver.assert_fold_language()

    @allure.severity('blocker')
    @pytest.mark.parametrize('language, lg, title', getExcelAllData('语言', 'Admin/login.xlsx'))
    def test_010(self, language, lg, title):
        allure.dynamic.title(f'切换{language}语言测试')
        allure.dynamic.tag(language)
        self.driver.click_unfold_language()
        self.driver.click_language(lg)
        self.driver.assert_switch_language(title)
