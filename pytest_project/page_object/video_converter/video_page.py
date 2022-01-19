from pytest_project.config.conf import cm
from pytest_project.page.basepage import WebPage
import allure
from pytest_project.common.readelement import Element, get_values_in_name, get_branch_all_value, get_any_key_info

video = Element('VideoConverter/body')


class VideoPage(WebPage):

    @allure.step('点击下载按钮')
    def download_video(self, loc):
        self.is_click(loc)

    @allure.step('点击购买按钮')
    def goto_buy(self, loc):
        self.is_click(loc)

    @staticmethod
    def is_download():
        """判断下载是否成功"""
        return cm.get_download_filename() == 'crdownload' or cm.get_download_filename() == 'pkg' or cm.\
            get_download_filename() == 'exe'

    def is_goto_buy(self):
        """判断跳转购买页面内容与实际相同"""
        return self.find_element(video['buy-class']) is not None

    def is_index(self):
        """判断是否跳转产品首页"""
        return self.find_element(video['index-handle']) is not None

    def is_goto_tech(self):
        """判断是否跳转技巧页面"""
        return self.find_element(video['tech-handle']) is not None

    def is_goto_guide(self):
        """判断是否跳转guide页面"""
        return self.find_element(video['guide-handle']) is not None

    def is_menu_skip_if(self, i):
        """根据索引判断断言"""
        if i == 0:
            return self.is_index()
        if i == 1:
            return self.is_goto_tech()
        if i == 2:
            return self.is_goto_guide()
        if i == 3:
            return self.is_download()
        if i == 4:
            return self.is_goto_buy()

    def return_conversion_handle(self):
        return self.element_text(video['conversion-handle']) == 'Video Conversion'

    @allure.step('页面滑动到menu上')
    def scroll_to_menu(self):
        """移动到menu栏"""
        self.scroll_to_loc(video['menu-class'])

    @allure.step('点击menu下的按钮')
    def click_menu_button(self, i):
        """
        点击menu下的按钮
        i:menu第几个按钮
        """
        self.is_click(get_branch_all_value().get_branch_all_value(video.data, 'menu')[i])

    @allure.step('点击editing切换按钮')
    def click_editing_button(self, index):
        """点击editing按钮"""
        self.is_click(get_values_in_name().get_values_in_name(video.data, index)[0])

    def return_editing_image_class(self, index):
        """判断轮播图的class值"""
        return 'active' in self.getAttribute(get_values_in_name().get_values_in_name(video.data, index)[1], 'class')

    @allure.step('点击文章链接')
    def click_container_link(self, article_name):
        """点击文章链接"""
        self.is_click(get_any_key_info(article_name, video.data))

    @allure.step('切换轮播图')
    def click_carousel(self):
        """点击评论轮播图下的索引按钮"""
        self.is_click(video['carousel-li'])

    def return_carousel_index(self):
        """获取当前评论轮播图的索引"""
        return self.getAttribute(video['carousel-inner'], 'class') == 'item active'

    def return_container_enhancement_handle(self):
        """获取标题"""
        return self.element_text(video['container-handle']) == 'Video Enhancement'

    def is_goto_article(self, article_name):
        """判断是否跳转文章页面"""
        return self.find_element(video['article-body']) is not None and article_name.replace('-', ' ') in \
               self.element_text(video['article-handle']).lower()

    @allure.step('页面滑动到conversion上')
    def scroll_to_conversion(self):
        """移动到conversion栏"""
        self.scroll_to_loc(video['conversion-class'])

    @allure.step('页面滑动到editing上')
    def scroll_to_editing(self):
        """移动到editing栏"""
        self.scroll_to_loc(video['editing-class'])

    @allure.step('页面滑动到container_enhancement上')
    def scroll_to_container_enhancement(self):
        """移动到container栏"""
        self.scroll_to_loc(video['enhancement-class'])

    @allure.step('页面滑动到carousel上')
    def scroll_to_carousel(self):
        """移动到carousel栏"""
        self.scroll_to_loc(video['carousel-comment-class'])

    @allure.step('页面滑动到container_enhancement上')
    def scroll_to_container_article(self):
        """移动到container栏"""
        self.scroll_to_loc(video['container-article-class'])
