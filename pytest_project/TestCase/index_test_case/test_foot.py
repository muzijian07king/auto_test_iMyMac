import allure
import pytest
from pytest_project.common.readconfig import ini
from pytest_project.page_object.index.foot_page import FootPage
from pytest_project.common.readelement import Element
from pytest_project.common.readexcel import getExcelAllData, getExcelOneCol

language = Element('index/language')
foot = Element('index/foot')


@allure.feature('首页测试')
@allure.story('底部链接栏测试')
@allure.severity('blocker')
class TestFoot(object):

    @pytest.fixture(scope='function', autouse=True)
    def open_index(self, drivers):
        self.driver = FootPage(drivers)
        self.driver.get_url(ini.url)
        self.driver.jsInDriver('document.documentElement.scrollTop=10000')

    @pytest.mark.parametrize('link,url', getExcelAllData('底部链接', 'index/index.xlsx'))
    def test_001(self, link, url):
        """点击底部链接"""
        allure.dynamic.title('测试点击底部超链接：{}'.format(link))
        self.driver.click_link(link)
        allure.dynamic.tag('点击底部超链接')
        allure.dynamic.link(url, name=link)
        self.driver.assert_link(url)

    @pytest.mark.parametrize('lge,url', getExcelAllData('切换语言', 'index/index.xlsx'))
    @allure.severity('critical')
    def test_002(self, lge, url):
        """切换语言"""
        allure.dynamic.tag('语言切换为{}'.format(language.getLanguage(lge)))
        allure.dynamic.title('切换语言==》{}'.format(language.getLanguage(lge)))
        self.driver.click_drop_down_option()
        self.driver.switch_language(lge)
        self.driver.assert_switch_language(lge, url)

    @pytest.mark.parametrize('email', getExcelOneCol('正确邮箱', 1, 'index/index.xlsx'))
    def test_003(self, email):
        """提交邮箱订阅更新以及优惠"""
        allure.dynamic.tag('订阅信息')
        allure.dynamic.title('正确提交订阅测试')
        self.driver.input_email(email)
        self.driver.click_submit()
        self.driver.assert_submit_email()

    @pytest.mark.parametrize('email', getExcelOneCol('错误邮箱', 1, 'index/index.xlsx'))
    @allure.severity('critical')
    def test_004(self, email):
        """提交邮箱订阅更新以及优惠"""
        allure.dynamic.tag('订阅')
        allure.dynamic.title('提交错误邮箱测试')
        self.driver.input_email(email)
        self.driver.click_submit()
        self.driver.assert_fail_submit_email()

    @allure.title('测试著作权')
    @allure.tag('著作权')
    @allure.severity('critical')
    def test_005(self):
        """著作权"""
        self.driver.scroll_copyright()
        self.driver.assert_copyright()

    @allure.title('测试授权隐私')
    @allure.tag('ok按钮')
    @allure.severity('critical')
    def test_006(self):
        self.driver.click_ok_use_cookie()
        self.driver.assert_use_cookie()

    @allure.title('测试跳转隐私页面')
    @allure.tag('隐私文章')
    @allure.severity('critical')
    def test_007(self):
        self.driver.click_privacy_link()
        self.driver.assert_goto_privacy()
