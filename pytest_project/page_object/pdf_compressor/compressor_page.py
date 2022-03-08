import allure

from pytest_project.page.basepage import WebPage
from pytest_project.common.readconfig import cm
from pytest_project.common.readelement import Element

PDF = Element('PDFCompressor/body')


class CompressorPage(WebPage):

    @allure.step('下载topper栏的PDF-Compressor')
    def click_topper_download(self):
        self.is_click(PDF.readYaml('$.download.handle'))

    @allure.step('下载container栏的PDF-Compressor')
    def click_container_download(self):
        self.is_click(PDF.readYaml('$.download.foot'))

    @allure.step('移动到container栏')
    def scroll_container(self):
        self.jsInDriver('document.documentElement.scrollTop=3300')

    def assert_download(self):
        result = 'pkg' in cm.get_download_filename() or 'crdownload' in cm.get_download_filename()
        self.allure_assert_step('判断是否下载成功', result)
        assert result
