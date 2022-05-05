import random
import time
import allure
from pytest_project.utils.times import sleep
from pytest_project.page.basepage import WebPage
from pytest_project.common.readelement import Element

retrieve = Element('Retrieve/retrieve')


class RegisterPage(WebPage):
    email = str(time.time()).split('.')[0] + '@qq.com'
    name = f'admin{random.randint(100, 999)}'
    password = f'{random.randint(10000000, 99999999)}'

    @allure.step('进入login页面')
    def goto_login(self):
        self.is_click(retrieve.readYaml('$.index.login'))

    def goto_register(self):
        self.is_click(retrieve.readYaml('$.index.register'))

    def assert_goto_login(self):
        self.allure_assert('判断是否进入登录页面', ('not_eq', self.find_element(retrieve.readYaml('$.login.forgot')), None),
                           ('eq', self.get_current_url(), 'https://member.imymac.com/login'))

    def assert_goto_register(self):
        self.allure_assert('判断是否进入注册页面', ('eq', self.get_current_url(), 'https://member.imymac.com/register'))

    def assert_email(self):
        self.allure_assert('判断邮箱是否正确', (
            'eq', self.getAttribute(retrieve.readYaml('$.index.email'), 'href'), 'mailto:support@imymac.com'))

    @allure.step('输入用户名')
    def input_name(self, name):
        self.input_text(retrieve.readYaml('$.register.username'), name)

    @allure.step('输入邮箱')
    def input_email(self, email):
        self.input_text(retrieve.readYaml('$.register.usereamil'), email)

    @allure.step('输入密码')
    def input_password(self, password):
        self.input_text(retrieve.readYaml('$.register.userpwd'), password)

    @allure.step('输入确认密码')
    def input_userdbpwd(self, password):
        self.input_text(retrieve.readYaml('$.register.userdbpwd'), password)

    @allure.step('勾选隐私框')
    def check_accept(self):
        self.is_click(retrieve.readYaml('$.register.accept-button'))

    @allure.step('点击login按钮')
    def click_login(self):
        self.is_click(retrieve.readYaml('$.register.login'))

    @allure.step('点击register按钮')
    def click_register(self):
        self.is_click(retrieve.readYaml('$.register.register'), 0)

    def assert_error_name(self):
        self.allure_assert('判断用户名错误提示信息', ('eq', self.is_display(retrieve.readYaml('$.register.error.name')), True))

    def assert_error_email(self):
        self.allure_assert('判断邮箱错误提示信息', ('eq', self.is_display(retrieve.readYaml('$.register.error.email')), True))

    def assert_error_pwd_length(self):
        self.allure_assert('判断密码长度错误提示信息',
                           ('eq', self.is_display(retrieve.readYaml('$.register.error.pwd.length')), True))

    def assert_error_pwd_space(self):
        self.allure_assert('判断密码空格错误提示信息',
                           ('eq', self.is_display(retrieve.readYaml('$.register.error.pwd.space')), True))

    def assert_error_re_pwd(self):
        self.allure_assert('判断重新输入密码错误提示信息',
                           ('eq', self.is_display(retrieve.readYaml('$.register.error.re-pwd')), True))

    def assert_error_accept(self):
        self.allure_assert('判断隐私授权错误提示信息', ('eq', self.is_display(retrieve.readYaml('$.register.error.accept')), True))

    @allure.step('跳转到隐私条款页面')
    def goto_terms(self):
        self.is_click(retrieve.readYaml('$.register.terms'))

    def assert_goto_terms(self):
        self.allure_assert('判断是否跳转隐私条款页面', ('eq', self.get_current_url(), 'https://www.imymac.com/terms.html'))

    def assert_register_failed(self):
        self.allure_assert('判断注册失败提示信息', ('not_eq', self.find_element(retrieve.readYaml('$.register.failed')), None))

    def assert_register_succeed(self):
        self.allure_assert('判断是否弹出注册成功提示信息', ('eq', self.is_display(retrieve.readYaml('$.register.succeed')), True))
        sleep(3)
        self.allure_assert('判断是否跳转登录页面', ('not_eq', self.find_element(retrieve.readYaml('$.login.forgot')), None),
                           ('eq', self.get_current_url(), 'https://member.imymac.com/login'))

    @allure.step('点击语言按钮展开语言选择框')
    def click_unfold_language(self):
        self.is_click(retrieve.readYaml('$.language.switch'))

    def assert_unfold_language(self):
        self.allure_assert('判断展开语言选择框', ('eq', self.is_display(retrieve.readYaml('$.language.selector')), True))

    @allure.step('点击语言按钮折叠语言选择框')
    def click_fold_language(self):
        self.click_unfold_language()
        self.jsInDriver("document.querySelector('div.select-lang>p').click()")

    def assert_fold_language(self):
        self.allure_assert('判断折叠语言选择框', ('eq', self.is_display(retrieve.readYaml('$.language.selector')), False))

    @allure.step('点击语言')
    def click_language(self, language):
        self.is_click(retrieve.readYaml(f'$.language.{language}'), 1)

    def assert_switch_language(self, title):
        self.allure_assert('判断切换语言是否成功', ('eq', self.element_text(retrieve.readYaml('$.language.title')), title))
