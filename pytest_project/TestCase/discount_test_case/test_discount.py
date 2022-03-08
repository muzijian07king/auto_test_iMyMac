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
        allure.dynamic.tag(step)
        self.driver.assert_step_context(step, context)

    @allure.title('步骤邮箱链接测试')
    @allure.severity('critical')
    @allure.tag('步骤中邮箱')
    def test_002(self):
        self.driver.assert_step_email()

    @allure.title('底部邮箱链接测试')
    @allure.severity('critical')
    @allure.tag('底部邮箱')
    def test_003(self):
        self.driver.assert_email()

    @allure.title('支持优惠邮箱测试')
    @allure.tag('优惠邮箱')
    @allure.severity('trivial')
    def test_004(self):
        self.driver.assert_discount_email(getExcelOneCol('支持优惠邮箱', 1, 'Discount/discount.xlsx'))
