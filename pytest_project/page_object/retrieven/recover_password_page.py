import allure
from pytest_project.page.basepage import WebPage
from pytest_project.common.readelement import Element

retrieve = Element('Retrieve/retrieve')


class RecoverPage(WebPage):
    def assert_goto_login(self):
        result = self.get_current_url() == 'https://member.imymac.com/login'
        self.allure_assert_step('判断是否进入登录页面', result)
        assert result

    @allure.step('输入邮箱')
    def input_email(self, email):
        self.input_text(retrieve.readYaml('$.recover.email'), email)

    @allure.step('点击login按钮')
    def click_login(self):
        self.is_click(retrieve.readYaml('$.recover.login'))

    @allure.step('点击recover按钮')
    def click_recover(self):
        self.is_click(retrieve.readYaml('$.recover.recover'))

    def assert_error_popup(self):
        result = self.is_display(retrieve.readYaml('$.recover.error'))
        self.allure_assert_step('判断弹出邮箱错误提示信息', result)
        assert result

    def assert_recover_succeed(self):
        self.element_if_display(retrieve.readYaml('$.recover.succeed'))
        result = self.is_display(retrieve.readYaml('$.recover.succeed'))
        self.allure_assert_step('判断成功发送找回密码邮件提示信息', result)
        assert result

    def assert_recover_failed(self):
        result = self.is_display(retrieve.readYaml('$.recover.failed'))
        self.allure_assert_step('判断发送失败找回密码邮件提示信息', result)
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
