import allure
import pytest

from pytest_project.page_object.pdf_compressor.compressor_page import CompressorPage
from pytest_project.common.readconfig import ini
from pytest_project.common.readelement import Element, get_branch_all_value

compressor = Element('PDFCompressor/body')


@allure.feature('pdf-compressor页面测试')
@allure.story('pdf-compressor页面内容测试')
class TestBody(object):
    @pytest.fixture(scope='function', autouse=True)
    def openurl(self, drivers):
        self.driver = CompressorPage(drivers)
        self.driver.get_url(ini.get_url('pdf-compressor'))
        self.driver.click_sale_off_link()

    @pytest.mark.parametrize('download', get_branch_all_value().get_branch_all_value(compressor.data, 'free-download'))
    @allure.title('下载compressor测试')
    @allure.tag('下载compressor')
    @allure.severity('blocker')
    def test_001(self, download):
        self.driver.click_download(download)
        assert self.driver.is_download
