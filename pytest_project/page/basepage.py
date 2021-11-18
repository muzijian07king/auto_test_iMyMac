"""
selenium基类
存放selenium基类的封装方法
"""
import requests
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from pytest_project.config.conf import cm
from pytest_project.utils.times import sleep
from pytest_project.utils.logger import log
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from selenium import webdriver


class WebPage(object):

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 30
        self.wait = WebDriverWait(self.driver, self.timeout)

    def get_url(self, url):
        """打开网址并验证"""
        self.driver.set_page_load_timeout(300)
        try:
            self.driver.get(url)
            self.driver.implicitly_wait(10)
            log.info("打开网页{}".format(url))
        except TimeoutException:
            raise TimeoutException('打开%s超时请检查网络或网站服务器' % url)

    @staticmethod
    def element_locator(func, loc):
        """元素定位器"""
        name, value = loc
        return func(cm.LOCATE_MODE[name], value)

    def element_loc(self, loc):
        name, value = loc
        return cm.LOCATE_MODE[name], value

    def find_element(self, loc):
        """定位单个元素"""
        try:
            WebPage.element_locator(lambda *args: self.wait.until(EC.presence_of_element_located(args)), loc)
            method, func = self.element_loc(loc)
            """
            method : 定位方法 例如id定位法
            func : 根据方法定位元素
            """
            return self.driver.find_element(method, func)
        except AttributeError:
            raise AttributeError('未找到{}元素'.format(loc))

    def find_elements(self, loc):
        """定位多个元素"""
        try:
            WebPage.element_locator(lambda *args: self.wait.until(EC.presence_of_all_elements_located(args)), loc)
            method, func = self.element_loc(loc)
            """
            method : 定位方法 例如id定位法
            func : 根据方法定位元素
            """
            return self.driver.find_elements(method, func)
        except AttributeError:
            raise AttributeError('未找到{}元素'.format(loc))

    def element_num(self, loc):
        number = len(self.find_elements(loc))
        log.info("相同元素：{}".format((loc, number)))
        return number

    def input_text(self, loc, text):
        """输入"""
        ele = self.find_element(loc)
        ele.clear()
        ele.send_keys(text)
        log.info('输入文本：{}'.format(text))
        # try:
        #     assert self.element_txet(loc) == text
        # except Exception:
        #     raise Exception('未输入成功')

    def is_click(self, loc):
        self.find_element(loc).click()
        log.info('点击元素：{}'.format(loc))
        sleep()

    def element_txet(self, loc):
        """获取当前的text属性"""
        _text = self.find_element(loc).text
        log.info('获取到文本：{}'.format(_text))
        return _text

    def move_element(self, loc):
        """鼠标悬停到某元素"""
        ele = self.find_element(loc)
        log.info('鼠标悬停在{}'.format(loc))
        ActionChains(self.driver).move_to_element(ele).perform()

    def get_current_url(self):
        """获取当前页面url"""
        return self.driver.current_url

    def Key_enter(self, loc):
        """模拟回车键"""
        ele = self.find_element(loc)
        ele.send_keys(Keys.ENTER)
        log.info("按下回车")

    @property
    def get_source(self):
        """获取页面源代码"""
        return self.driver.page_source

    def refresh(self):
        """刷新页面"""
        self.driver.refresh()
        log.info('刷新页面')
        self.driver.implicitly_wait(30)

    def getAttribute(self, loc, attribute):
        """
        定位到元素后获取属性值
        :param loc: 元素
        :param attribute: 属性值
        :return:
        """
        attr = self.find_element(loc)
        log.info('获取到{}元素的值==》{}'.format(attribute, attr.get_attribute(attribute)))
        return attr.get_attribute(attribute)

    def getAttributes(self, loc, attribute):
        """
        定位到多元素获取属性值
        :param loc: 元素
        :param attribute: 属性值
        :return:
        """
        attr = self.find_elements(loc)
        context = []
        for i in attr:
            context.append(i.get_attribute(attribute))
            log.info('获取到{}元素的值==》{}'.format(attribute, i.get_attribute(attribute)))
        return context

    def jsInDriver(self, js):
        """使用js"""
        log.info('使用js操控浏览器==》{}'.format(js))
        sleep()
        self.driver.execute_script(js)

    def scroll_to_loc(self, loc):
        """下拉滑动到某个元素上"""
        log.info("页面滚到元素{}".format(loc))
        div = self.find_element(loc)
        self.driver.execute_script('arguments[0].scrollIntoView()', div)
        sleep()
        self.jsInDriver('document.documentElement.scrollBy(0,1)')
        sleep()

    def scroll_to_loc_is_click(self, loc):
        """下拉滑动到某个元素上"""
        log.info("页面滚到元素{}".format(loc))
        div = self.find_element(loc)
        self.driver.execute_script('arguments[0].scrollIntoView()', div)
        self.jsInDriver('document.documentElement.scrollBy(0,1)')
        sleep(0.5)
        div.click()

    def is_request_200(self):
        request_data = requests.get(self.get_current_url())
        log.info('当前响应码为{}'.format(request_data))
        return request_data == 200

    def switch_to_frame(self, frame):
        log.info('切换frame==>{}'.format(frame))
        self.driver.switch_to.frame(frame)

    def select_by_value(self, loc, value):
        """选择option"""
        log.info('下拉框value选择==》{}'.format(value))
        Select(self.find_element(loc)).select_by_value(value)

    def select_by_index(self, loc, index):
        """选择option"""
        log.info('下拉框索引选择==》{}'.format(index))
        Select(self.find_element(loc)).select_by_index(index)

    def select_by_text(self, loc, text):
        """选择option"""
        log.info('下拉框值选择==》{}'.format(text))
        Select(self.find_element(loc)).select_by_visible_text(text)

    def select_option_text(self, loc):
        """获取选中的value"""
        option_value = Select(self.find_element(loc)).first_selected_option.text
        log.info('当前选中的选项是==》{}'.format(option_value))
        return option_value

    def elements_text(self, loc):
        """获取多个元素的text"""
        ele = self.find_elements(loc)
        texts = []
        for i in ele:
            texts.append(i.text)
        log.info('获取到text==》{}'.format(texts))
        return texts

    def element_if_display(self, loc):
        """显形等待元素可见"""
        log.info('等待元素可见==》{}'.format(loc[1]))
        self.wait.until(EC.visibility_of_element_located(self.element_loc(loc)))

    def get_diver_title(self):
        """获取网页标签页标题"""
        log.info('获取到title==>{}'.format(self.driver.title))
        return self.driver.title

    def click_sale_off_link(self):
        """关闭黑色星期五链接"""
        log.info('关闭黑色星期五优惠链接')
        self.jsInDriver("document.querySelector('div.close-tag').click()")
