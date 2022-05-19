from pytest_project.config.conf import cm
from pytest_project.page.basepage import WebPage
import allure
from pytest_project.common.readelement import Element

video = Element('VideoConverter/body')


class VideoPage(WebPage):

    @allure.step('点击下载按钮')
    def download_video(self):
        self.is_click(video['download'])

    @allure.step('点击购买按钮')
    def goto_buy(self):
        self.is_click(video['buy'])

    @allure.step('切换win系统')
    def switch_win(self):
        pass
        # self.is_click(video.readYaml('$.os.win'))

    @allure.step('切换mac系统')
    def switch_mac(self):
        self.is_click(video.readYaml('$.os.mac'))

    @allure.step('移动到技巧栏')
    def scroll_tip(self):
        self.jsInDriver('document.documentElement.scrollTop=4700')

    def click_tip_link(self, index, name):
        with allure.step(f'点击技巧文章：{name}'):
            self.is_click(video.readYaml(f'$.tips.tip-{index}'))

    @allure.step("滑动到2200纵坐标弹出导航栏")
    def popup_navbar(self):
        self.jsInDriver('document.documentElement.scrollTop=2000')
        self.jsInDriver('document.documentElement.scrollTop=2200')

    @allure.step("点击logo")
    def click_logo(self):
        self.is_click(video.readYaml('$.nav.logo'))

    @allure.step("点击导航栏上的下载按钮")
    def click_download(self):
        self.is_click(video.readYaml('$.nav.download'))

    @allure.step("点击导航栏上的购买按钮")
    def click_buy(self):
        self.is_click(video.readYaml('$.nav.buy'))

    def assert_switch_win(self):
        self.allure_assert('判断是否切换成win',
                           ('eq', self.getAttribute(video.readYaml('$.os.win'), 'class'), "version-win active"),
                           ('eq', self.getAttribute(video['download'], 'class'), "btn blue try-it-free win"),
                           ('eq', self.getAttribute(video['buy'], 'class'), 'btn orange win'))

    def assert_switch_mac(self):
        self.allure_assert('判断是否切换成mac',
                           ('eq', self.getAttribute(video.readYaml('$.os.mac'), 'class'), "version-mac active"),
                           ('eq', self.getAttribute(video['download'], 'class'), "btn blue try-it-free"),
                           ('eq', self.getAttribute(video['buy'], 'class'), 'btn orange'))

    def assert_download_win(self):
        """判断下载win端是否成功"""
        suffix = cm.get_download_filename()
        self.allure_assert_or('判断是否下载win端成功', ('eq', suffix, 'crdownload'), ('eq', suffix, 'exe'))

    def assert_download_mac(self):
        """判断下载mac端是否成功"""
        suffix = cm.get_download_filename()
        self.allure_assert_or('判断是否下载mac端成功', ('eq', suffix, 'crdownload'), ('eq', suffix, 'pkg'),
                              ('eq', suffix, 'dmg'))

    def assert_goto_buy(self):
        """判断跳转购买页面内容与实际相同"""
        self.allure_assert('判断是否跳转购买页面',
                           ('eq', self.get_current_url(), 'https://www.imymac.com/store/buy-video-converter.html'))

    def assert_goto_tip(self, url):
        """判断是否跳转技巧文章页面"""
        self.allure_assert('判断是否跳转购买页面', ('eq', self.get_current_url(), url))

    def assert_index(self):
        """判断是否跳转首页"""
        self.allure_assert('判断是否跳转首页', ('eq', self.get_current_url(), 'https://www.imymac.com/video-converter/'))
