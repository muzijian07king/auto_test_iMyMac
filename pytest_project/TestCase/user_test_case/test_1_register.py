import time

import allure
import pytest
from pytest_project.common.readconfig import ini

from pytest_project.page_object.retrieven.register_page import RegisterPage
from pytest_project.common.readexcel import getExcelAllData, set_excel_data


@allure.feature('用户系统测试')
@allure.severity('critical')
class TestBody(object):
    email = str(time.time()).split('.')[0] + '@qq.com'

    @pytest.fixture(scope='function', autouse=True)
    def open_url(self, drivers):
        self.driver = RegisterPage(drivers)
        self.driver.get_url(ini.get_url('register'))
        self.driver.click_unfold_language()
        self.driver.click_language('en')

    @pytest.fixture(scope='function')
    def save_email(self):
        yield
        set_excel_data('注册成功', 'Admin/register.xlsx', 2, 2, self.email)

    @allure.title('注册成功测试')
    @allure.tag('注册成功')
    @allure.severity('blocker')
    @allure.story('注册页面功能测试')
    @pytest.mark.parametrize('name,email,pwd,re_pwd', getExcelAllData('注册成功', 'Admin/register.xlsx'))
    @pytest.mark.flaky(reruns=0)
    def test_001(self, name, email, pwd, re_pwd, save_email):
        self.driver.input_name(name)
        email = self.email
        self.driver.input_email(email)
        self.driver.input_password(pwd)
        self.driver.input_userdbpwd(re_pwd)
        self.driver.check_accept()
        self.driver.click_register()
        self.driver.assert_register_succeed()

    @allure.title('注册时输入错误用户名测试')
    @allure.tag('用户名错误')
    @allure.severity('critical')
    @allure.story('注册页面功能测试')
    @pytest.mark.parametrize('name,email,pwd,re_pwd', getExcelAllData('注册用户名错误', 'Admin/register.xlsx'))
    def test_002(self, name, email, pwd, re_pwd):
        self.driver.input_name(name)
        self.driver.input_email(email)
        self.driver.input_password(pwd)
        self.driver.input_userdbpwd(re_pwd)
        self.driver.click_register()
        self.driver.assert_error_name()

    @allure.title('注册时输入错误邮箱测试')
    @allure.tag('邮箱错误')
    @allure.severity('critical')
    @allure.story('注册页面功能测试')
    @pytest.mark.parametrize('name,email,pwd,re_pwd', getExcelAllData('注册邮箱错误', 'Admin/register.xlsx'))
    def test_003(self, name, email, pwd, re_pwd):
        self.driver.input_name(name)
        self.driver.input_email(email)
        self.driver.input_password(pwd)
        self.driver.input_userdbpwd(re_pwd)
        self.driver.click_register()
        self.driver.assert_error_email()

    @allure.title('注册时输入错误密码测试')
    @allure.tag('密码空格错误')
    @allure.severity('critical')
    @allure.story('注册页面功能测试')
    @pytest.mark.parametrize('name,email,pwd,re_pwd', getExcelAllData('注册密码空格错误', 'Admin/register.xlsx'))
    def test_004(self, name, email, pwd, re_pwd):
        self.driver.input_name(name)
        self.driver.input_email(email)
        self.driver.input_password(pwd)
        self.driver.input_userdbpwd(re_pwd)
        self.driver.click_register()
        self.driver.assert_error_pwd_space()

    @allure.title('注册时输入错误密码测试')
    @allure.tag('密码长度错误')
    @allure.severity('critical')
    @allure.story('注册页面功能测试')
    @pytest.mark.parametrize('name,email,pwd,re_pwd', getExcelAllData('注册密码长度错误', 'Admin/register.xlsx'))
    def test_005(self, name, email, pwd, re_pwd):
        self.driver.input_name(name)
        self.driver.input_email(email)
        self.driver.input_password(pwd)
        self.driver.input_userdbpwd(re_pwd)
        self.driver.click_register()
        self.driver.assert_error_pwd_length()

    @allure.title('注册时输入错误确认密码测试')
    @allure.tag('确认密码错误')
    @allure.severity('critical')
    @allure.story('注册页面功能测试')
    @pytest.mark.parametrize('name,email,pwd,re_pwd', getExcelAllData('注册确认密码错误', 'Admin/register.xlsx'))
    @pytest.xfail('待修复')
    def test_006(self, name, email, pwd, re_pwd):
        self.driver.input_name(name)
        self.driver.input_email(email)
        self.driver.input_password(pwd)
        self.driver.input_userdbpwd(re_pwd)
        self.driver.click_register()
        self.driver.assert_error_re_pwd()

    @allure.title('输入已注册的邮箱注册失败测试')
    @allure.tag('输入已注册的邮箱')
    @allure.severity('critical')
    @allure.story('注册页面功能测试')
    @pytest.mark.parametrize('name,email,pwd,re_pwd', getExcelAllData('注册失败', 'Admin/register.xlsx'))
    def test_007(self, name, email, pwd, re_pwd):
        self.driver.input_name(name)
        self.driver.input_email(email)
        self.driver.input_password(pwd)
        self.driver.input_userdbpwd(re_pwd)
        self.driver.check_accept()
        self.driver.click_register()
        self.driver.assert_register_failed()

    @allure.title('未勾选隐私条款测试')
    @allure.tag('未勾选隐私条款')
    @allure.severity('blocker')
    @allure.story('注册页面功能测试')
    def test_008(self):
        self.driver.click_register()
        self.driver.assert_error_accept()

    @allure.title('跳转登录页面测试')
    @allure.tag('跳转登录页面')
    @allure.severity('blocker')
    @allure.story('注册页面功能测试')
    def test_009(self):
        self.driver.click_login()
        self.driver.assert_goto_login()

    @allure.title('跳转隐私文章测试')
    @allure.tag('跳转隐私文章')
    @allure.severity('blocker')
    @allure.story('注册页面功能测试')
    def test_010(self):
        self.driver.goto_terms()
        self.driver.assert_goto_terms()

    @allure.title('展开语言选择框测试')
    @allure.tag('展开语言')
    @allure.severity('blocker')
    @allure.story('注册页面功能测试')
    def test_011(self):
        self.driver.click_unfold_language()
        self.driver.assert_unfold_language()

    @allure.title('折叠语言选择框测试')
    @allure.tag('折叠语言')
    @allure.severity('blocker')
    @allure.story('注册页面功能测试')
    def test_012(self):
        self.driver.click_fold_language()
        self.driver.assert_fold_language()

    @allure.severity('blocker')
    @allure.story('注册页面功能测试')
    @pytest.mark.parametrize('language, lg, title', getExcelAllData('语言', 'Admin/register.xlsx'))
    def test_013(self, language, lg, title):
        allure.dynamic.title(f'切换{language}语言测试')
        allure.dynamic.tag(language)
        self.driver.click_unfold_language()
        self.driver.click_language(lg)
        self.driver.assert_switch_language(title)
