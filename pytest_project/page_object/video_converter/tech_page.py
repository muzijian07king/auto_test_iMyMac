from pytest_project.config.conf import cm
from pytest_project.page.basepage import WebPage
import allure
from pytest_project.common.readelement import Element, get_any_key_info

tech = Element('VideoConverter/tech-specification')


class TechPage(WebPage):

    @allure.step('下载video')
    def click_download(self):
        self.is_click(tech['download'])

    @allure.step('点击购买按钮')
    def goto_buy(self):
        self.is_click(tech['buy'])

    def assert_download(self):
        """判断下载是否成功"""
        suffix = cm.get_download_filename()
        result = suffix == 'crdownload' or suffix == 'pkg' or suffix == 'exe'
        self.allure_assert_step('判断下载是否成功', result)
        assert result

    def assert_goto_buy(self):
        """判断跳转购买页面内容与实际相同"""
        result = self.get_current_url() == 'https://www.imymac.com/store/buy-video-converter.html'
        self.allure_assert_step('判断跳转购买页面内容与实际相同', result)
        assert result
