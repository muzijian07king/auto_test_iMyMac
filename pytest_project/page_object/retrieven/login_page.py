import allure
from pytest_project.page.basepage import WebPage
from pytest_project.common.readelement import Element
from pytest_project.utils.times import sleep

retrieve = Element('Retrieve/retrieve')


class LoginPage(WebPage):
    def assert_goto_register(self):
        result = self.get_current_url() == 'https://member.imymac.com/register'
        self.allure_assert_step('判断是否进入注册页面', result)
        assert result

    @allure.step('输入邮箱')
    def input_email(self, email):
        self.input_text(retrieve.readYaml('$.login.email'), email)

    @allure.step('输入密码')
    def input_password(self, password):
        self.input_text(retrieve.readYaml('$.login.password'), password)

    @allure.step('勾选记住我')
    def check_remember(self):
        self.is_click(retrieve.readYaml('$.login.remember'))

    def assert_check_remember(self):
        result = self.getAttribute(retrieve.readYaml('$.login.remember'), 'class') == 'rem-checkbox rem-click'
        self.allure_assert_step('判断是否勾选记住我按钮', result)
        assert result

    def assert_remember_function(self):
        result = self.get_cookie(Element('User/cookie').readYaml('$.name', 1)) is not None
        self.allure_assert_step('判断记住我功能是否实现', result)
        assert result

    @allure.step('取消勾选记住我')
    def cancel_check_remember(self):
        self.check_remember()
        self.is_click(retrieve.readYaml('$.login.remember'))

    def assert_cancel_check_remember(self):
        result = self.getAttribute(retrieve.readYaml('$.login.remember'), 'class') == 'rem-checkbox'
        self.allure_assert_step('判断是否取消勾选记住我按钮', result)
        assert result

    @allure.step('点击login按钮')
    def click_login(self):
        self.is_click(retrieve.readYaml('$.login.login'))

    @allure.step('点击register按钮')
    def click_register(self):
        self.is_click(retrieve.readYaml('$.login.register'))

    def assert_error_popup(self):
        result = self.is_display(retrieve.readYaml('$.login.error'))
        self.allure_assert_step('判断弹出登录失败错误信息', result)
        assert result

    @allure.step('跳转到找回密码页面')
    def goto_forgot(self):
        self.is_click(retrieve.readYaml('$.login.forgot'))

    def assert_goto_forgot(self):
        result = self.get_current_url() == 'https://member.imymac.com/forgot'
        self.allure_assert_step('判断是否跳转找回密码页面', result)
        assert result

    def assert_login_succeed(self, name):
        result = self.element_text(retrieve.readYaml('$.login.succeed')) == name
        self.allure_assert_step('判断登录成功提示信息', result)
        assert result

    @allure.step('点击语言按钮展开语言选择框')
    def click_unfold_language(self):
        self.is_click(retrieve.readYaml('$.language.switch'))

    def assert_unfold_language(self):
        result = self.is_display(retrieve.readYaml('$.language.selector'))
        self.allure_assert_step('判断展开语言选择框', result)
        assert result

    @allure.step('点击语言按钮折叠语言选择框')
    def click_fold_language(self):
        self.click_unfold_language()
        self.jsInDriver("document.querySelector('div.select-lang>p').click()")

    def assert_fold_language(self):
        result = not self.is_display(retrieve.readYaml('$.language.selector'))
        self.allure_assert_step('判断折叠语言选择框', result)
        assert result

    @allure.step('点击语言')
    def click_language(self, language):
        self.is_click(retrieve.readYaml(f'$.language.{language}'))

    def assert_switch_language(self, title):
        result = self.element_text(retrieve.readYaml('$.language.title')) == title
        self.allure_assert_step('判断切换语言是否成功', result)
        assert result
