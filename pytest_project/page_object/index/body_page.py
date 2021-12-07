import allure
from pytest_project.page.basepage import WebPage
from pytest_project.common.readelement import Element, get_any_key_info, get_branch_all_value
from pytest_project.utils.times import sleep

body = Element('index/body')


class BodyPage(WebPage):

    @allure.step('点击左箭头')
    def click_carousel_left_button(self):
        """点击产品滚动栏的左箭头"""
        self.is_click(body['left-carousel-control'])
        sleep(2)

    @allure.step('点击右箭头')
    def click_carousel_right_button(self):
        """点击滚动栏的右箭头"""
        self.is_click(body['right-carousel-control'])
        sleep(2)

    @allure.step('点击下载按钮')
    def click_ppm_download(self):
        """点击ppm下载按钮"""
        self.is_click(get_branch_all_value().get_branch_all_value(body.data, 'PowerMyMac')[0])

    @allure.step('点击下载按钮')
    def click_video_download(self):
        """点击video下载按钮"""
        self.is_click(get_branch_all_value().get_branch_all_value(body.data, 'video')[0])

    @allure.step('点击详细按钮')
    def click_ppm_more(self):
        """点击ppm详细按钮"""
        self.is_click(get_branch_all_value().get_branch_all_value(body.data, 'PowerMyMac')[1])

    @allure.step('点击详细按钮')
    def click_video_more(self):
        """点击video详细按钮"""
        self.is_click(get_branch_all_value().get_branch_all_value(body.data, 'video')[1])

    @allure.step('点击链接')
    def click_link(self, link):
        """点击功能介绍链接"""
        self.is_click(get_any_key_info(link, body.data))

    @allure.step('点击左箭头')
    def click_media_left_button(self):
        """点击评价滚动栏的左箭头"""
        self.is_click(body['media-left'])

    @allure.step('点击右箭头')
    def click_media_right_button(self):
        """点击评价滚动栏的右箭头"""
        self.is_click(body['media-right'])

    @allure.step('获取内容')
    def get_choose_p(self):
        """获取choose标题内容来判断是否加载成功"""
        self.element_txet(body['chooseItemBox'])

    @allure.step('判断轮播图是否滚动')
    def return_carousel_class(self):
        """返回产品轮播图当前div的class属性"""
        return self.getAttribute(body['carousel'], 'class')

    @allure.step('判断轮播图是否滚动')
    def return_media_class(self):
        """返回评价轮播图当前div的class属性"""
        return self.getAttribute(body['media'], 'class')

    @allure.step('页面滑动到评价轮播图')
    def scroll_to_media(self):
        """页面移动到评价轮播图"""
        js = 'document.documentElement.scrollTop=1760'
        self.jsInDriver(js)
        sleep()

    def scroll_top(self):
        """回到顶点"""
        self.scroll_to_media()
        with allure.step('点击去顶部按钮'):
            self.is_click(body['top-button'])
            sleep()

    @allure.step('判断是否到达顶部')
    def return_whether_top(self):
        return self.getAttribute(body['top-button'], 'class') == 'top-btn t4s'

    @allure.step('判断是否存在container')
    def return_container_whether_null(self):
        return self.find_element(body['container']) is not None
