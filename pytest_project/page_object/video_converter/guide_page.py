from pytest_project.config.conf import cm
from pytest_project.page.basepage import WebPage
import allure
from pytest_project.common.readelement import Element

guide = Element('VideoConverter/guide')


class GuidePage(WebPage):

    @allure.step('下载video')
    def click_download(self):
        self.is_click(guide['download'])

    @allure.step('点击购买按钮')
    def goto_buy(self):
        self.is_click(guide['buy'])

    @allure.step('切换win指南')
    def cut_win_guide(self):
        self.is_click(guide.readYaml('$.os.win'))

    @allure.step('切换mac指南')
    def cut_mac_guide(self):
        self.is_click(guide.readYaml('$.os.mac'))

    def assert_download(self):
        """判断下载是否成功"""
        result = cm.get_download_filename() == 'crdownload' or cm.get_download_filename() == 'pkg' or cm. \
            get_download_filename() == 'exe'
        self.allure_assert_step('判断下载是否成功', result)
        assert result

    def assert_goto_buy(self):
        """判断跳转购买页面内容与实际相同"""
        result = self.get_current_url() == 'https://www.imymac.com/store/buy-video-converter.html'
        self.allure_assert_step('判断跳转购买页面内容与实际相同', result)
        assert result

    def assert_goto_win_guide(self):
        """判断是否跳转到win指南"""
        result = self.getAttribute(guide.readYaml('$.os.win'), 'class') == "version-tag win active"
        self.allure_assert_step('判断是否跳转到win指南', result)
        assert result

    def assert_goto_mac_guide(self):
        """判断是否跳转到mac指南"""
        result = self.getAttribute(guide.readYaml('$.os.mac'), 'class') == "version-tag mac active"
        self.allure_assert_step('判断是否跳转到mac指南', result)
        assert result

    @allure.step('移动到指南栏')
    def scroll_guide(self):
        self.scroll_to_loc(guide.readYaml('$.nav.div'))

    def click_guide(self, no):
        with allure.step(f'点击指南{no}'):
            self.is_click(guide.readYaml(f'$.nav.{no}'))

    def assert_goto_guide(self, style: str):
        result = self.getAttribute(guide.readYaml('$.nav.div'), 'style') == style
        self.allure_assert_step('判断是否跳转到指定指南上', result)
        assert result
