import allure

from pytest_project.page.basepage import WebPage
from pytest_project.common.readconfig import cm


class CompressorPage(WebPage):

    @allure.step('下载PDF-Compressor')
    def click_download(self, loc):
        self.is_click(loc)

    @property
    @allure.step('判断下载是否成功启动')
    def is_download(self):
        return 'pkg' in cm.get_download_filename() or 'crdownload' in cm.get_download_filename()


