import allure
import pytest
from pytest_project.page_object.profile.profile_page import ProfilePage
from pytest_project.common.readconfig import ini


@allure.feature('团体简介页面测试')
@allure.story('功能测试')
class TestBody(object):
    @pytest.fixture(scope='function', autouse=True)
    def open_url(self, drivers):
        self.driver = ProfilePage(drivers)
        self.driver.get_url(ini.get_url('profiles'))
        self.driver.close_cookie_popup()

    @allure.title('跳转左侧作者详情页面测试')
    @allure.tag('左侧作者')
    @allure.severity('critical')
    def test_001(self):
        name = self.driver.goto_left_writer()
        self.driver.assert_goto_writer(name)

    @allure.title('跳转中间作者详情页面测试')
    @allure.tag('中间作者')
    @allure.severity('critical')
    def test_002(self):
        name = self.driver.goto_mid_writer()
        self.driver.assert_goto_writer(name)

    @allure.title('跳转右侧作者详情页面测试')
    @allure.tag('右侧作者')
    @allure.severity('critical')
    def test_003(self):
        name = self.driver.goto_right_writer()
        self.driver.assert_goto_writer(name)

    @allure.title('左侧作者详情页面查看第一篇文章页面测试')
    @allure.tag('左侧作者')
    @allure.severity('critical')
    def test_004(self):
        self.driver.goto_left_writer()
        title = self.driver.click_articles()
        self.driver.assert_goto_articles(title)

    @allure.title('左侧作者详情页面查看第一篇科学技术文章页面测试')
    @allure.tag('左侧作者')
    @allure.severity('critical')
    def test_005(self):
        self.driver.goto_left_writer()
        self.driver.click_tech()
        self.driver.assert_goto_tech()

    @allure.title('左侧作者详情页面点击第一篇科学技术更多按钮测试')
    @allure.tag('左侧作者')
    @allure.severity('critical')
    def test_006(self):
        self.driver.goto_left_writer()
        self.driver.click_more()
        self.driver.assert_goto_tech()

    @allure.title('中间作者详情页面查看第一篇文章页面测试')
    @allure.tag('中间作者')
    @allure.severity('critical')
    def test_007(self):
        self.driver.goto_mid_writer()
        title = self.driver.click_articles()
        self.driver.assert_goto_articles(title)

    @allure.title('中间作者详情页面查看第一篇科学技术文章页面测试')
    @allure.tag('中间作者')
    @allure.severity('critical')
    def test_008(self):
        self.driver.goto_mid_writer()
        self.driver.click_tech()
        self.driver.assert_goto_tech()

    @allure.title('中间作者详情页面点击第一篇科学技术更多按钮测试')
    @allure.tag('中间作者')
    @allure.severity('critical')
    def test_009(self):
        self.driver.goto_mid_writer()
        self.driver.click_more()
        self.driver.assert_goto_tech()

    @allure.title('右侧作者详情页面查看第一篇文章页面测试')
    @allure.tag('右侧作者')
    @allure.severity('critical')
    def test_010(self):
        self.driver.goto_right_writer()
        title = self.driver.click_articles()
        self.driver.assert_goto_articles(title)

    @allure.title('右侧作者详情页面查看第一篇科学技术文章页面测试')
    @allure.tag('右侧作者')
    @allure.severity('critical')
    def test_011(self):
        self.driver.goto_right_writer()
        self.driver.click_tech()
        self.driver.assert_goto_tech()

    @allure.title('右侧作者详情页面点击第一篇科学技术更多按钮测试')
    @allure.tag('右侧作者')
    @allure.severity('critical')
    def test_012(self):
        self.driver.goto_right_writer()
        self.driver.click_more()
        self.driver.assert_goto_tech()