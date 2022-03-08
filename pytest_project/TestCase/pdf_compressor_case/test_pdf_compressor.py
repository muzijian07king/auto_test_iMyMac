import allure
import pytest

from pytest_project.page_object.pdf_compressor.compressor_page import CompressorPage
from pytest_project.common.readconfig import ini


@allure.feature('pdf-compressor页面测试')
@allure.story('pdf-compressor页面内容测试')
class TestBody(object):
    @pytest.fixture(scope='function', autouse=True)
    def openurl(self, drivers):
        self.driver = CompressorPage(drivers)
        self.driver.get_url(ini.get_url('pdf-compressor'))

    @allure.title('下载compressor测试')
    @allure.tag('topper')
    @allure.severity('blocker')
    def test_001(self):
        self.driver.click_topper_download()
        self.driver.assert_download()

    @allure.title('下载compressor测试')
    @allure.tag('container')
    @allure.severity('blocker')
    def test_002(self):
        self.driver.click_container_download()
        self.driver.assert_download()
