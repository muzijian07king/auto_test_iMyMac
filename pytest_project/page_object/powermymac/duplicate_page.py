import allure
from pytest_project.page.basepage import WebPage
from pytest_project.common.readelement import Element
from pytest_project.config.conf import cm

duplicate = Element('PowerMyMac/common')


class DuplicatePage(WebPage):
    @allure.step('点击container栏的下载按钮')
    def download_container_ppm(self):
        """点击下载按钮"""
        self.is_click(duplicate['container-download'], 1)

    @allure.step('点击container栏的购买')
    def goto_container_buy(self):
        """去购买页面"""
        self.is_click(duplicate['container-buy'])

    @allure.step('移动到技巧栏')
    def scroll_tip(self):
        self.scroll_to_loc(duplicate['tip'])

    def click_link(self, index: int, name):
        """点击技巧文章"""
        with allure.step(f'点击技巧文章链接:{name}'):
            self.is_click(duplicate.readYaml(f'$.tips.tip-{index}'))

    @allure.step('点击summary栏的下载按钮')
    def download_summary_ppm(self):
        """点击下载按钮"""
        self.is_click(duplicate['summary-download'], 1)

    @allure.step('移动到summary栏')
    def scroll_summary(self):
        self.jsInDriver('document.documentElement.scrollTop=4300')

    @allure.step('点击summary栏的购买')
    def goto_summary_buy(self):
        """去购买页面"""
        self.is_click(duplicate['summary-buy'])

    @allure.step('滑动到2000纵坐标')
    def popup_nav(self):
        self.jsInDriver('document.documentElement.scrollTop=2000')
        self.jsInDriver('document.documentElement.scrollTop=2200')

    @allure.step('点击navbar栏的下载按钮')
    def download_navbar_ppm(self):
        """点击下载按钮"""
        self.is_click(duplicate['navbar-download'], 1)

    @allure.step('点击navbar栏的购买')
    def goto_navbar_buy(self):
        """去购买页面"""
        self.is_click(duplicate['navbar-buy'])

    @allure.step('点击navbar栏的logo')
    def goto_index(self):
        """进入mac uninstaller页面"""
        self.jsInDriver("document.querySelector('div.navbar-sub-header>a:nth-child(1)').click()")

    def assert_download(self):
        self.allure_assert_or('判断是否下载成功', ('eq', cm.get_download_filename(), 'crdownload'),
                              ('eq', cm.get_download_filename(), 'pkg'))

    def assert_go_buy(self):
        self.allure_assert('判断是否跳转购买页面',
                           ('eq', self.get_current_url(), 'https://www.imymac.com/store/buy-powermymac.html'))

    def assert_tip_html(self, url):
        self.allure_assert('判断是否跳转技巧页面', ('eq', self.get_current_url(), url))

    def assert_index(self):
        self.allure_assert('判断是否跳转pmm主页', ('eq', self.get_current_url(), 'https://www.imymac.com/powermymac/'))

    def assert_popup_nav(self):
        self.allure_assert('判断是否弹出导航栏', ('eq', self.is_display(duplicate['navbar']), True))
