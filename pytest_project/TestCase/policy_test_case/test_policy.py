import allure

from pytest_project.page_object.protocol.context_page import ProtocolPage
import pytest
from pytest_project.common.readexcel import getExcelOneCol, getSheetNames, getValueByIndex
from pytest_project.common.readconfig import ini


@allure.feature('协议内容测试')
@allure.story('文章测试')
@allure.severity('minor')
class TestBody(object):
    @pytest.fixture(scope='function', autouse=True)
    def open_url(self, drivers):
        self.driver = ProtocolPage(drivers)
        self.driver.get_url(ini.url)

    @pytest.mark.parametrize('sheet_name', getSheetNames('Protocol/protocol.xlsx'))
    @allure.title('大标题测试')
    def test_001(self, sheet_name):
        allure.dynamic.tag('{}的标题'.format(sheet_name))
        self.driver.goto_protocol(sheet_name)
        assert self.driver.if_headline(getValueByIndex(1, 2, sheet_name, 'Protocol/protocol.xlsx'))

    @allure.title('小标题测试')
    @pytest.mark.parametrize('sheet_name', getSheetNames('Protocol/protocol.xlsx'))
    def test_002(self, sheet_name):
        allure.dynamic.tag('{}的标题'.format(sheet_name))
        self.driver.goto_protocol(sheet_name)
        assert self.driver.if_title(getExcelOneCol(sheet_name, 2, 'Protocol/protocol.xlsx'))

    @allure.title('邮箱链接测试')
    @allure.severity('normal')
    @pytest.mark.parametrize('sheet_name',
                             list(filter(lambda name: name != 'refund', getSheetNames('Protocol/protocol.xlsx'))))
    def test_003(self, sheet_name):
        allure.dynamic.tag('{}的邮箱链接'.format(sheet_name))
        self.driver.goto_protocol(sheet_name)
        assert self.driver.if_email_in_context()
