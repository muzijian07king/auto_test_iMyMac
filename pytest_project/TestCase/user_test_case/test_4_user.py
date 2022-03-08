import allure
import pytest
from pytest_project.common.readconfig import ini
from pytest_project.common.readexcel import getValueByIndex, getExcelAllData, getExcelByRow
from pytest_project.page_object.user.user_page import UserPage
from pytest_project.common.readconfig import cm
import random


@allure.feature('用户中心测试')
@allure.story('个人中心')
@allure.severity('critical')
class TestBody(object):
    @pytest.fixture(scope='function', autouse=True)
    def open_url(self, drivers):
        self.driver = UserPage(drivers)
        self.driver.get_url(ini.get_url('login'))
        self.driver.add_member_imymac_cookie()
        self.driver.get_url(ini.get_url('user'))
        self.driver.click_unfold_language()
        self.driver.click_language('en')

    @pytest.fixture(scope='function')
    def login_out(self):
        yield
        self.driver.login_out_end_step(getValueByIndex(2, 2, '注册成功', 'Admin/register.xlsx'),
                                       getValueByIndex(3, 2, '注册成功', 'Admin/register.xlsx'))
        self.driver.update_member_imymac_cookie(
            self.driver.get_cookie('remember_dashboard_59ba36addc2b2f9401580f014c7f58ea4e30989d'))

    @allure.title('判断是否进入个人中心')
    @allure.severity('blocker')
    def test_001(self):
        email = getValueByIndex(2, 2, '注册成功', 'Admin/register.xlsx')
        self.driver.assert_profile(email)

    @allure.story('个人中心')
    @allure.title('用户更换头像测试')
    @allure.tag('成功更换头像')
    @allure.severity('blocker')
    def test_002(self):
        self.driver.change_photo(cm.Photo)
        self.driver.submit_info_changes()
        self.driver.assert_succeed_change_photo()

    @allure.story('个人中心')
    @allure.title('用户更换头像测试')
    @allure.tag('更换头像失败')
    def test_003(self):
        self.driver.change_photo(cm.not_image)
        self.driver.submit_info_changes()
        self.driver.assert_failed_change_photo()

    @allure.story('个人中心')
    @allure.title('切换账户栏测试')
    @allure.tag('账户栏')
    def test_004(self):
        self.driver.switch_password()
        self.driver.switch_account()
        self.driver.assert_switch_account()

    @allure.story('个人中心')
    @allure.title('切换修改密码栏测试')
    @allure.tag('密码栏')
    def test_005(self):
        self.driver.switch_password()
        self.driver.assert_switch_password()

    @allure.title('修改用户名测试')
    @allure.tag('成功修改用户名')
    @allure.severity('blocker')
    def test_006(self):
        name = f'admin{random.randint(0, 10000)}'
        self.driver.input_name(name)
        self.driver.submit_info_changes()
        self.driver.assert_succeed_change_name(name)

    @allure.title('修改用户名测试')
    @allure.tag('修改用户名失败')
    def test_007(self):
        self.driver.input_name(' ')
        self.driver.submit_info_changes()
        self.driver.assert_failed_change_name()

    @allure.title('修改密码测试')
    @allure.tag('修改失败原密码为空')
    def test_008(self):
        self.driver.switch_password()
        self.driver.input_current_password('')
        self.driver.submit_password_changes()
        self.driver.assert_input_current_password()

    @allure.title('修改密码测试')
    @allure.tag('修改失败原密码错误')
    @pytest.mark.parametrize('old_password,new_password,confirm_password', getExcelAllData('原密码错误', 'Admin/user.xlsx'))
    def test_009(self, old_password, new_password, confirm_password):
        self.driver.switch_password()
        self.driver.input_current_password(old_password)
        self.driver.input_new_password(new_password)
        self.driver.input_confirm_password(confirm_password)
        self.driver.submit_password_changes()
        self.driver.assert_failed_change_password()

    @allure.title('修改密码测试')
    @allure.tag('修改失败新密码格式错误')
    @pytest.mark.parametrize('old_password,new_password,confirm_password', getExcelAllData('新密码错误', 'Admin/user.xlsx'))
    def test_010(self, old_password, new_password, confirm_password):
        self.driver.switch_password()
        self.driver.input_current_password(old_password)
        self.driver.input_new_password(new_password)
        self.driver.input_confirm_password(confirm_password)
        self.driver.submit_password_changes()
        self.driver.assert_input_new_password()

    @allure.title('修改密码测试')
    @allure.tag('修改失败再次输入密码格式错误')
    @pytest.mark.parametrize('old_password,new_password,confirm_password',
                             getExcelAllData('再次输入密码错误', 'Admin/user.xlsx'))
    def test_011(self, old_password, new_password, confirm_password):
        self.driver.switch_password()
        self.driver.input_current_password(old_password)
        self.driver.input_new_password(new_password)
        self.driver.input_confirm_password(confirm_password)
        self.driver.submit_password_changes()
        self.driver.assert_input_confirm_password()

    @allure.title('修改密码测试')
    @allure.tag('修改密码长度为8成功')
    @allure.severity('blocker')
    @pytest.mark.parametrize('new_password,confirm_password', getExcelByRow('修改成功', 1, 1, 'Admin/user.xlsx'))
    @pytest.mark.flaky(reruns=0)
    def test_012(self, new_password, confirm_password):
        old_password = getValueByIndex(3, 2, '注册成功', 'Admin/register.xlsx')
        email = getValueByIndex(2, 2, '注册成功', 'Admin/register.xlsx')
        self.driver.switch_password()
        self.driver.input_current_password(old_password)
        self.driver.input_new_password(new_password)
        self.driver.input_confirm_password(confirm_password)
        self.driver.submit_password_changes()
        self.driver.assert_succeed_change_password(email, new_password)

    @allure.title('修改密码测试')
    @allure.tag('修改密码长度为18成功')
    @allure.severity('blocker')
    @pytest.mark.parametrize('new_password,confirm_password', getExcelByRow('修改成功', 2, 1, 'Admin/user.xlsx'))
    @pytest.mark.flaky(reruns=0)
    def test_013(self, new_password, confirm_password):
        old_password = getValueByIndex(3, 2, '注册成功', 'Admin/register.xlsx')
        email = getValueByIndex(2, 2, '注册成功', 'Admin/register.xlsx')
        self.driver.switch_password()
        self.driver.input_current_password(old_password)
        self.driver.input_new_password(new_password)
        self.driver.input_confirm_password(confirm_password)
        self.driver.submit_password_changes()
        self.driver.assert_succeed_change_password(email, new_password)

    @allure.title('跳转忘记密码测试')
    @allure.tag('跳转忘记密码成功')
    @allure.severity('blocker')
    def test_014(self):
        self.driver.switch_password()
        self.driver.goto_forgot()
        self.driver.assert_goto_forgot()

    @allure.title('弹出退出框测试')
    @allure.tag('弹出退出框')
    @allure.severity('blocker')
    def test_015(self):
        self.driver.popup_logout()
        self.driver.assert_popup_logout()

    @allure.title('关闭退出框测试')
    @allure.tag('关闭退出框')
    @allure.severity('blocker')
    def test_016(self):
        self.driver.close_popup_logout()
        self.driver.assert_close_popup_logout()

    @allure.title('展开语言选择框测试')
    @allure.tag('展开语言')
    @allure.severity('blocker')
    def test_017(self):
        self.driver.click_unfold_language()
        self.driver.assert_unfold_language()

    @allure.title('折叠语言选择框测试')
    @allure.tag('折叠语言')
    @allure.severity('blocker')
    def test_018(self):
        self.driver.click_fold_language()
        self.driver.assert_fold_language()

    @allure.severity('blocker')
    @pytest.mark.parametrize('language, lg, title', getExcelAllData('语言', 'Admin/user.xlsx'))
    def test_019(self, language, lg, title):
        allure.dynamic.title(f'切换{language}语言测试')
        allure.dynamic.tag(language)
        self.driver.click_unfold_language()
        self.driver.click_language(lg)
        self.driver.assert_switch_language(title)

    @allure.title('折叠左侧导航栏测试')
    @allure.tag('折叠')
    def test_020(self):
        self.driver.click_close_icon()
        self.driver.assert_fold_inner()

    @allure.title('展开左侧导航栏测试')
    @allure.tag('展开')
    def test_021(self):
        self.driver.click_unfold_icon()
        self.driver.assert_unfold_inner()

    @allure.title('跳转我的订阅页面测试')
    @allure.tag('跳转我的订阅')
    @allure.severity('blocker')
    def test_022(self):
        self.driver.goto_subscription()
        self.driver.assert_goto_subscription()

    @allure.title('跳转个人信息页面测试')
    @allure.tag('跳转我的订阅')
    @allure.severity('blocker')
    def test_023(self):
        self.driver.goto_profile()
        self.driver.assert_goto_profile()

    @allure.title('退出个人中心测试')
    @allure.tag('退出')
    @allure.severity('blocker')
    def test_024(self, login_out):
        self.driver.popup_logout()
        self.driver.click_logout()
        self.driver.assert_logout()
