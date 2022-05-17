import allure
from pytest_project.utils.times import get_utctime, sleep
from pytest_project.page.basepage import WebPage
from pytest_project.common.readelement import Element
from pytest_project.common.readconfig import ini
from pytest_project.common.readexcel import set_excel_data

user = Element('User/user')


class UserPage(WebPage):

    def assert_profile(self, email):
        sleep(2)
        self.allure_assert('判断cookie登录是否成功', ('eq', self.element_text(user.readYaml("Profile.Account.email")), email))

    @allure.step('更换头像')
    def change_photo(self, file):
        self.input_file(user.readYaml("Profile.change-photo"), file)

    @allure.step('提交个人信息的修改')
    def submit_info_changes(self):
        self.is_click(user.readYaml("Profile.Account.changes-button"))

    @allure.step('提交密码的修改')
    def submit_password_changes(self):
        self.is_click(user.readYaml("Profile.New-Password.changes-button"), 2)

    def assert_succeed_change_photo(self):
        self.allure_assert('判断是否弹出上传成功提示', ('eq', self.is_display(user.readYaml("Profile.Account.succeed")), True))
        self.refresh()
        sleep()
        self.allure_assert('判断刷新后头像是否显示', (
            'include', f'https://member.imymac.com/images/avatar/{get_utctime("%Y%m%d%H")}',
            self.getAttribute(user.readYaml("Profile.headling-img"), 'src')))

    def assert_failed_change_photo(self):
        self.allure_assert('判断弹出头像上传失败信息', ('eq', self.is_display(user.readYaml("Profile.Account.failed")), True))

    @allure.step('切换到account栏')
    def switch_account(self):
        self.is_click(user.readYaml("Profile.Account.account-icon"), 1)

    @allure.step('切换到password栏')
    def switch_password(self):
        self.is_click(user.readYaml("Profile.New-Password.password-icon"), 1)

    def assert_switch_account(self):
        self.allure_assert('判断是否切换到account栏', (
            'eq', self.getAttribute(user.readYaml("Profile.Account.account-icon"), 'class'),
            'nav-pro-item account-icon active'))

    def assert_switch_password(self):
        self.allure_assert('判断是否切换到password栏', (
            'eq', self.getAttribute(user.readYaml("Profile.New-Password.password-icon"), 'class'),
            'nav-pro-item password-icon active'))

    @allure.step('输入用户名')
    def input_name(self, name):
        self.is_click(user.readYaml('Profile.Account.name'))
        self.input_text(user.readYaml('Profile.Account.name'), name)

    def assert_failed_change_name(self):
        self.allure_assert('判断弹出用户名失败信息', ('eq', self.is_display(user.readYaml("Profile.Account.name-error")), True))

    def assert_succeed_change_name(self, name):

        result = self.allure_assert('判断用户名修改成功',
                                    ('eq', self.is_display(user.readYaml("Profile.Account.succeed")), True),
                                    ('eq', self.element_text(user.readYaml("Profile.name")), name))
        if result:
            set_excel_data('注册成功', 'Admin/register.xlsx', 1, 2, name)

    @allure.step('输入原始密码')
    def input_current_password(self, password):
        self.input_text(user.readYaml("Profile.New-Password.current-password"), password)

    @allure.step('输入新密码')
    def input_new_password(self, password):
        self.input_text(user.readYaml("Profile.New-Password.new-password"), password)

    @allure.step('输入第二遍新密码')
    def input_confirm_password(self, password):
        self.input_text(user.readYaml("Profile.New-Password.confirm-password"), password)

    def assert_input_current_password(self):
        self.allure_assert('判断弹出旧密码为空错误信息',
                           ('eq', self.is_display(user.readYaml("Profile.New-Password.current-error")), True))

    def assert_input_new_password(self):
        self.allure_assert('判断弹出新密码错误信息',
                           ('eq', self.is_display(user.readYaml("Profile.New-Password.new-error")), True))

    def assert_input_confirm_password(self):
        self.allure_assert('判断弹出再次输入密码错误信息',
                           ('eq', self.is_display(user.readYaml("Profile.New-Password.confirm-error")), True))

    def assert_failed_change_password(self):
        self.allure_assert('判断弹出旧密码错误信息', ('eq', self.is_display(user.readYaml("Profile.New-Password.failed")), True), (
            'eq', self.element_text(user.readYaml('$.Profile.New-Password.current-error')), 'Password Wrong'))

    @allure.step('修改密码后置步骤')
    def login_end_step(self, email, password):
        self.input_text(user.readYaml('$.email'), email)
        self.input_text(user.readYaml('$.password'), password)
        self.is_click(user.readYaml('$.login'), 4)

    @allure.step('退出登录后置步骤')
    def login_out_end_step(self, email, password):
        self.input_text(user.readYaml('$.email'), email)
        self.input_text(user.readYaml('$.password'), password)
        self.is_click(user['remember'])
        self.is_click(user.readYaml('$.login'), 5)
        assert self.find_element(user.readYaml('$.succeed')) is not None

    def assert_succeed_change_password(self, email, password):
        result1 = self.allure_assert('判断是否弹出修改密码成功', (
            'not_eq', self.find_element(user.readYaml("$.Profile.New-Password.succeed")), None))
        result2 = None
        if result1:
            self.get_url(ini.get_url('login'))
            self.login_end_step(email, password)
            result2 = self.allure_assert('判断修改密码后是否能登录成功',
                                         ('eq', self.get_current_url(), 'https://member.imymac.com/user/edit'))
        result = result1 and result2
        if result:
            set_excel_data('注册成功', 'Admin/register.xlsx', 3, 2, password)
            set_excel_data('注册成功', 'Admin/register.xlsx', 4, 2, password)

    @allure.step('跳转到忘记密码页面')
    def goto_forgot(self):
        self.is_click(user.readYaml('$.Profile.New-Password.forgot'))

    def assert_goto_forgot(self):
        self.allure_assert('判断是否跳转到忘记密码页面', ('eq', self.get_current_url(), 'https://member.imymac.com/forgot'))

    @allure.step('点击用户弹出退出框')
    def popup_logout(self):
        self.is_click(user.readYaml('$.nav.name'))

    @allure.step('点击退出按钮')
    def click_logout(self):
        self.is_click(user.readYaml('$.nav.logout'))

    def assert_popup_logout(self):
        self.allure_assert('判断是否弹出退出按钮', ('eq', self.is_display(user.readYaml('$.nav.logout')), True))

    def assert_logout(self):
        self.allure_assert('判断是否退出个人中心', ('eq', self.get_current_url(), 'https://member.imymac.com/login'))

    @allure.step('关闭用户退出框')
    def close_popup_logout(self):
        self.popup_logout()
        self.jsInDriver('document.querySelector("span.self-name").click()')

    def assert_close_popup_logout(self):
        self.allure_assert('判断是否关闭退出弹窗', ('eq', self.is_display(user.readYaml('$.nav.logout')), False))

    @allure.step('点击语言按钮展开语言选择框')
    def click_unfold_language(self):
        self.is_click(user.readYaml('$.nav.language.switch'))

    def assert_unfold_language(self):
        self.allure_assert('判断展开语言选择框', ('eq', self.is_display(user.readYaml('$.nav.language.selector')), True))

    @allure.step('点击语言按钮折叠语言选择框')
    def click_fold_language(self):
        self.click_unfold_language()
        self.jsInDriver("document.querySelector('div.select-lang>p').click()")

    def assert_fold_language(self):
        self.allure_assert('判断折叠语言选择框', ('eq', self.is_display(user.readYaml('$.nav.language.selector')), False))

    @allure.step('点击语言')
    def click_language(self, language):
        self.is_click(user.readYaml(f'$.nav.language.{language}'))

    def assert_switch_language(self, text):
        self.allure_assert('判断切换语言是否成功', ('eq', self.element_text(user.readYaml('$.flex-left.my-subscription')), text))

    @allure.step('点击折叠左侧导航栏按钮')
    def click_close_icon(self):
        self.is_click(user.readYaml('$.flex-left.close-icon'))

    def assert_fold_inner(self):
        self.allure_assert('判断折叠左侧导航栏成功', (
            'eq', self.getAttribute(user.readYaml('$.flex-left.inner'), 'class'), 'nav-bg trans-04 w-80'))

    @allure.step('展开左侧导航栏按钮')
    def click_unfold_icon(self):
        self.click_close_icon()
        self.jsInDriver("document.querySelector('div.flex>div:nth-child(1)>div:nth-child(1)>div>h1>i').click()")

    def assert_unfold_inner(self):
        self.allure_assert('判断展开左侧导航栏成功',
                           ('eq', self.getAttribute(user.readYaml('$.flex-left.inner'), 'class'), 'nav-bg trans-04'))

    @allure.step('跳转到我的订阅页面')
    def goto_subscription(self):
        self.is_click(user.readYaml('$.flex-left.my-subscription'))

    @allure.step('跳转到个人信息')
    def goto_profile(self):
        self.is_click(user.readYaml('$.flex-left.profile'))

    def assert_goto_subscription(self):
        self.allure_assert('判断跳转到我的订阅页面成功',
                           ('eq', self.get_current_url(), 'https://member.imymac.com/products/management'))

    def assert_goto_profile(self):
        self.allure_assert('判断跳转到个人信息页面成功', ('eq', self.get_current_url(), 'https://member.imymac.com/user/edit'))
