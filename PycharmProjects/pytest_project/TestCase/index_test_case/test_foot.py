import allure
import pytest
from pytest_project.common.readconfig import ini
from pytest_project.page_object.index.foot_page import FootPage
from pytest_project.common.readelement import Element, get_recursion_key

language = Element('index/language')
foot = Element('index/foot')


@allure.feature('首页测试')
@allure.story('底部超链接测试')
class TestFoot(object):

    @pytest.fixture(scope='function', autouse=True)
    def open_index(self, drivers):
        self.driver = FootPage(drivers)
        self.driver.get_url(ini.url)

    @pytest.mark.parametrize('link', get_recursion_key().get_recursion_key(foot.data)[:19])
    @allure.severity('critical')
    def test_001(self, link):
        """点击底部链接"""
        allure.dynamic.tag('点击链接{}'.format(link))
        self.driver.click_link(link)
        allure.dynamic.title('测试{}链接'.format(link))
        assert link.lower() in self.driver.get_current_url()

    @pytest.mark.parametrize('lge', get_recursion_key().get_recursion_key(language.data))
    @allure.severity('critical')
    def test_002(self, lge):
        """切换语言"""
        allure.dynamic.tag('语言切换为{}'.format(language.getLanguage(lge)))
        allure.dynamic.title('切换语言==》{}'.format(language.getLanguage(lge)))
        self.driver.click_drop_down_option()
        self.driver.switch_language(lge)
        assert lge.lower() in self.driver.get_current_url()

    @pytest.mark.parametrize('email, error_text', [('123.com', 'Email Format Error!'), ('', 'Please Enter the Email!')])
    def test_003(self, email, error_text):
        """提交邮箱订阅更新以及优惠"""
        allure.dynamic.tag('订阅')
        allure.dynamic.title('错误提交订阅测试')
        self.driver.sendEmail(email)
        self.driver.click_search_button()
        assert self.driver.errorText() == error_text

    @pytest.mark.parametrize('email, Success', [('123@qq.com', 'Successfully')])
    @allure.severity('critical')
    def test_004(self, email, Success):
        """提交邮箱订阅更新以及优惠"""
        allure.dynamic.tag('订阅')
        allure.dynamic.title('正确提交订阅测试')
        self.driver.sendEmail(email)
        self.driver.click_search_button()
        assert self.driver.button_text() == Success


