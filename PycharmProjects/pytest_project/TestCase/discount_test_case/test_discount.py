import allure
import pytest

from pytest_project.page_object.discount.discount_page import DiscountPage
from pytest_project.common.readconfig import ini
from pytest_project.common.readexcel import getExcelAllData, getExcelOneCol


@allure.feature('学生优惠申请页面测试')
@allure.story('功能测试')
class TestBody(object):
    @pytest.fixture(scope='function', autouse=True)
    def open_url(self, drivers):
        self.driver = DiscountPage(drivers)
        self.driver.get_url(ini.get_url('discount'))

    @pytest.mark.parametrize('step,context', getExcelAllData('步骤介绍', 'Discount/discount.xlsx'))
    @allure.title('步骤内容测试')
    @allure.severity('trivial')
    def test_001(self, step, context):
        allure.dynamic.tag('{}==>{}'.format(step, context))
        assert self.driver.step_if_ture(step, context)

    @allure.title('购买链接测试')
    @allure.tag('链接测试')
    @allure.link('https://www.imymac.com/store/', name='购买链接')
    @allure.severity('critical')
    def test_002(self):
        self.driver.click_store_link()
        assert self.driver.if_goto_store()

    @pytest.mark.parametrize('email,feedback', getExcelAllData('提交反馈信息', 'Discount/discount.xlsx'))
    @allure.title('提交邮箱测试')
    @allure.severity('critical')
    def test_003(self, email, feedback):
        allure.dynamic.tag('邮箱==》{}'.format(email))
        self.driver.input_EDU_email(email)
        self.driver.submit_email()
        assert self.driver.submit_feedback(feedback)

    @allure.title('打开邮箱工具测试')
    @allure.tag('链接测试')
    @allure.severity('critical')
    def test_004(self):
        assert self.driver.if_goto_send_email()

    @pytest.mark.skip('功能未完成')
    @allure.title('查询邮箱拥有优惠测试')
    @allure.severity('critical')
    def test_005(self, search):
        allure.dynamic.tag('输入邮箱==》{}'.format(search))
        self.driver.search_email(search)
        self.driver.click_search_button()

    @allure.title('支持优惠邮箱测试')
    @allure.tag('优惠邮箱')
    @allure.severity('trivial')
    def test_006(self):
        assert self.driver.discount_email(getExcelOneCol('支持优惠邮箱', 1, 'Discount/discount.xlsx'))
