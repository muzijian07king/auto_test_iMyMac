import allure
import pytest

from pytest_project.common.readexcel import getExcelAllData
from pytest_project.page_object.contact.index import ContactPage
from pytest_project.common.readconfig import ini


class TestBody(object):
    @pytest.fixture(scope='function', autouse=True)
    def open_url(self, drivers):
        self.driver = ContactPage(drivers)
        self.driver.get_url(ini.get_url('contact'))

    @allure.title('邮箱链接测试')
    @allure.tag('写邮件')
    def test_001(self):
        assert self.driver.get_send_email()

    @allure.title('简介栏内容测试')
    @pytest.mark.parametrize('title,context', getExcelAllData('简介', 'Contact/contact.xlsx'))
    def test_002(self, title, context):
        allure.dynamic.tag('{}栏的简介'.format(title))
        assert self.driver.get_contact_text(title) == context
