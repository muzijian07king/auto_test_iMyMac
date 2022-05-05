import allure
import pytest
from pytest_project.common.readconfig import ini
from pytest_project.page_object.retrieven.recover_password_page import RecoverPage
from pytest_project.common.readexcel import getExcelAllData, getExcelOneCol


@allure.feature('用户系统测试')
@allure.story('找回密码页面功能测试')
@allure.severity('critical')
class TestBody(object):

    @pytest.fixture(scope='function', autouse=True)
    def open_url(self, drivers):
        self.driver = RecoverPage(drivers)
        self.driver.get_url(ini.get_url('recover'))

    @pytest.fixture(scope='function')
    def clear_cookie(self):
        self.driver.delete_all_cookie()
        self.driver.refresh()

    @pytest.fixture(scope='function')
    def switch_language(self):
        self.driver.click_unfold_language()
        self.driver.click_language('en')

    @allure.title('输入错误邮箱找回密码测试')
    @allure.severity('critical')
    @allure.tag('输入错误邮箱')
    @pytest.mark.parametrize('email', getExcelOneCol('邮箱错误', 1, 'Admin/recover.xlsx'))
    def test_001(self, email, switch_language, clear_cookie):
        self.driver.input_email(email)
        self.driver.click_recover()
        self.driver.assert_recover_failed()

    @allure.title('找回密码发送邮件成功测试')
    @allure.tag('发送成功')
    @allure.severity('blocker')
    @pytest.mark.parametrize('email', getExcelOneCol('邮箱正确', 1, 'Admin/recover.xlsx'))
    def test_002(self, email, switch_language):
        self.driver.input_email(email)
        self.driver.click_recover()
        self.driver.assert_recover_succeed()

    @allure.title('找回密码发送邮件失败测试')
    @allure.tag('发送失败')
    @allure.severity('blocker')
    @pytest.mark.parametrize('email', getExcelOneCol('邮箱为空', 1, 'Admin/recover.xlsx'))
    def test_003(self, email, switch_language):
        self.driver.input_email(email)
        self.driver.click_recover()
        self.driver.assert_error_popup()

    @allure.title('跳转登录页面测试')
    @allure.tag('跳转登录页面')
    @allure.severity('blocker')
    def test_004(self, switch_language):
        self.driver.click_login()
        self.driver.assert_goto_login()

    @allure.title('展开语言选择框测试')
    @allure.tag('展开语言')
    @allure.severity('blocker')
    def test_005(self):
        self.driver.click_unfold_language()
        self.driver.assert_unfold_language()

    @allure.title('折叠语言选择框测试')
    @allure.tag('折叠语言')
    @allure.severity('blocker')
    def test_006(self):
        self.driver.click_fold_language()
        self.driver.assert_fold_language()

    @allure.severity('blocker')
    @pytest.mark.parametrize('language, lg, title', getExcelAllData('语言', 'Admin/recover.xlsx'))
    def test_007(self, language, lg, title):
        allure.dynamic.title(f'切换{language}语言测试')
        allure.dynamic.tag(language)
        if language == '韩语' or language == '俄语':
            pytest.skip('语言转换失败')
        self.driver.click_unfold_language()
        self.driver.click_language(lg)
        self.driver.assert_switch_language(title)
