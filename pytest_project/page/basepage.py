"""
selenium基类
存放selenium基类的封装方法
"""
import json

import allure
import requests
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from pytest_project.config.conf import cm
from pytest_project.utils.times import sleep
from pytest_project.utils.logger import Log
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from pytest_project.common.readelement import Element

log = Log().get_log()


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
            self.driver.implicitly_wait(self.timeout)
            log.info("打开网页{}".format(url))
        except TimeoutException:
            raise TimeoutException('打开%s超时请检查网络或网站服务器' % url)

    @staticmethod
    def element_locator(func, loc):
        """元素定位器"""
        name, value = loc
        return func(cm.LOCATE_MODE[name], value)

    def find_element(self, loc):
        """定位单个元素"""
        try:
            element = WebPage.element_locator(lambda *args: self.wait.until(EC.presence_of_element_located(args)), loc)
            return element
        except AttributeError:
            raise AttributeError('未找到{}元素'.format(loc))

    def find_elements(self, loc):
        """定位多个元素"""
        try:
            elements = WebPage.element_locator(lambda *args: self.wait.until(EC.presence_of_all_elements_located(args)),
                                               loc)
            return elements
        except AttributeError:
            raise AttributeError('未找到{}元素'.format(loc))

    def element_num(self, loc):
        number = len(self.find_elements(loc))
        log.info("相同元素：{}".format((loc, number)))
        return number

    def element_text(self, loc) -> str:
        """获取当前的text属性"""
        _text = self.find_element(loc).text
        log.info('获取到文本：{}'.format(_text))
        return _text

    def input_text(self, loc, text):
        """输入"""
        ele = self.find_element(loc)
        ele.clear()
        log.debug('清理输入框')
        ele.send_keys(text)
        sleep(0.2)
        log.info('输入文本：{}'.format(text))

    def input_file(self, loc, file):
        """上传文件"""
        ele = self.find_element(loc)
        try:
            ele.send_keys(file)
            sleep(0.2)
            log.info('上传文件路径：{}'.format(file))
        except FileExistsError:
            log.error('文件不存在')

    def is_click(self, loc, s=0.5):
        """默认点击后暂停1s"""
        self.find_element(loc).click()
        log.info('点击元素：{}'.format(loc))
        sleep(s)

    def click_elements(self, loc, index='all'):
        """点击定位到的多个元素"""
        elements = self.find_elements(loc)
        if index == 'all':
            for ele in elements:
                ele.click()
                log.info('点击元素：{}'.format(ele))
        elif isinstance(index, int):
            elements[index].click()
            log.info('点击元素：{}'.format(elements[index]))
        sleep(0.2)

    def is_display(self, loc) -> bool:
        """判断元素是否可见"""
        ele = self.find_element(loc)
        display = ele.is_displayed()
        log.info(f'元素{loc}是否可见：{display}')
        return display

    def move_element(self, loc):
        """鼠标悬停到某元素"""
        ele = self.find_element(loc)
        log.info('鼠标悬停在{}'.format(loc))
        ActionChains(self.driver).move_to_element(ele).perform()

    def get_current_url(self):
        """获取当前页面url"""
        log.info(f'当前页面url：{self.driver.current_url}, 当前页面标题=》{self.driver.title}')
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

    def getAttribute(self, loc, attribute, s=0.1) -> str:
        """
        定位到元素后获取属性值
        :param loc: 元素
        :param attribute: 属性值
        :param s: 属性值
        :return:
        """
        sleep(s)
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
        log.info('获取到{}元素的值==》{}'.format(attribute, context))
        return context

    def jsInDriver(self, js, s=1):
        """使用js"""
        log.info('使用js操控浏览器==》{}'.format(js))
        result = self.driver.execute_script(js)
        sleep(s)
        if result is not None:
            log.info(f'浏览器控制台返回信息：{result}')
            return result

    def scroll_by_x_y(self, x, y):
        """
        以当前位置滑动（x，y）
        :param x: 横向滑动
        :param y: 纵向滑动
        :return:
        """
        self.jsInDriver(f'document.documentElement.scrollBy({x},{y})')

    def scroll_top(self, top):
        """页面下滑距顶部top大小"""
        log.info(f'页面下滑距顶部{top}')
        self.driver.execute_script(f"document.documentElement.scrollTop={top}")
        sleep()

    def scroll_to_loc(self, loc):
        """下拉滑动到某个元素上"""
        log.info("页面滚到元素{}".format(loc))
        div = self.find_element(loc)
        self.driver.execute_script('arguments[0].scrollIntoView()', div)
        sleep()

    def scroll_to_element(self, element):
        """
        滑动定位元素的位置
        :param element: find-element返回值
        :return:
        """
        log.info("页面滚到driverElement：{}".format(element))
        self.driver.execute_script('arguments[0].scrollIntoView()', element)

    def scroll_to_loc_is_click(self, loc, time=0.5):
        """下拉滑动到某个元素上点击"""
        log.info("页面滚到元素{}".format(loc))
        div = self.find_element(loc)
        self.driver.execute_script('arguments[0].scrollIntoView()', div)
        sleep(time)
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

    def get_diver_title(self):
        """获取网页标签页标题"""
        log.info('获取到title==>{}'.format(self.driver.title))
        return self.driver.title

    def input_alert(self, text):
        """浏览器提示框输入内容"""
        try:
            alert = self.driver.switch_to.alert
            alert.send_keys(text)
        except Exception as e:
            log.info('没有找到浏览器弹窗')
            log.error(e)

    def accept_alert(self):
        """弹窗点击确认"""
        try:
            alert = self.driver.switch_to.alert
            alert.accept()
        except Exception as e:
            log.info('没有找到浏览器弹窗')
            log.error(e)

    def dismiss_alert(self):
        """弹窗点击取消"""
        try:
            alert = self.driver.switch_to.alert
            alert.dismiss()
        except Exception as e:
            log.info('没有找到浏览器弹窗')
            log.error(e)

    def alert_text(self):
        """获取弹窗信息"""
        try:
            alert = self.driver.switch_to.alert
            text = alert.text()
            log.info(f'获取到文本:{text}')
            return text
        except Exception as e:
            log.info('没有找到浏览器弹窗')
            log.error(e)

    @staticmethod
    def allure_assert(title, *args):
        """
        进行断言
        :param title: 断言步骤名
        :param args: 已元组形式传参，(断言形式：[eq、not_eq、include、not_include、gt、ge、lt、le],
        eq参数实际在前,预期在后。include，子集在前，父集在后。[gt、ge、lt、le]，实际值在前，比较值在后)
        """
        index = 0
        results = []
        with allure.step(title):
            for arg in args:
                index += 1
                "断言形式"
                method = arg[0]
                "实际结果/子集/实际值"
                practical = arg[1]
                "预期结果/父集/比较值"
                expected = arg[2]
                if method == 'eq':
                    if expected is None:
                        result = practical is None
                    else:
                        result = expected == practical
                    allure.attach(json.dumps(f"预期结果: {expected},实际结果: {practical}", ensure_ascii=False, indent=2),
                                  f"第{index}个断言[相等]: {result}", allure.attachment_type.JSON)
                elif method == 'not_eq':
                    if expected is None:
                        result = practical is not None
                    else:
                        result = expected != practical
                    allure.attach(json.dumps(f"预期不相等: {expected},实际结果: {practical}", ensure_ascii=False, indent=2),
                                  f"第{index}个断言[不相等]: {result}", allure.attachment_type.JSON)
                elif method == 'include':
                    result = practical in expected
                    allure.attach(json.dumps(f"子集: {practical},父集: {expected}", ensure_ascii=False, indent=2),
                                  f"第{index}个断言[包含]: {result}", allure.attachment_type.JSON)
                elif method == 'not_include':
                    result = practical not in expected
                    allure.attach(json.dumps(f"子集: {practical},父集: {expected}", ensure_ascii=False, indent=2),
                                  f"第{index}个断言[不包含]: {result}", allure.attachment_type.JSON)
                elif method == 'ge':
                    result = practical >= expected
                    allure.attach(json.dumps(f"实际结果: {practical},比较值: {expected}", ensure_ascii=False, indent=2),
                                  f"第{index}个断言[大于等于]: {result}", allure.attachment_type.JSON)
                elif method == 'gt':
                    result = practical > expected
                    allure.attach(json.dumps(f"实际结果: {practical},比较值: {expected}", ensure_ascii=False, indent=2),
                                  f"第{index}个断言[大于]: {result}", allure.attachment_type.JSON)
                elif method == 'le':
                    result = practical <= expected
                    allure.attach(json.dumps(f"实际结果: {practical},比较值: {expected}", ensure_ascii=False, indent=2),
                                  f"第{index}个断言[小于等于]: {result}", allure.attachment_type.JSON)
                elif method == 'lt':
                    result = practical < expected
                    allure.attach(json.dumps(f"实际结果: {practical},比较值: {expected}", ensure_ascii=False, indent=2),
                                  f"第{index}个断言[小于]: {result}", allure.attachment_type.JSON)
                try:
                    log.info(f"预期结果: {expected},实际结果: {practical}, 断言方法：{method}, 断言结果：{result}")
                    results.append(result)
                except AssertionError:
                    raise AssertionError(
                        f'第{index}个断言[{method}]失败,实际结果{practical}|预期结果{expected}'
                    )
            assert False not in results
            return result

    @staticmethod
    def allure_assert_or(title, *args):
        """
        进行断言
        :param title: 断言步骤名
        :param args: 已元组形式传参，(断言形式：[eq、not_eq、include、not_include、gt、ge、lt、le],
        eq参数实际在前,预期在后。include，子集在前，父集在后。[gt、ge、lt、le]，实际值在前，比较值在后)
        """
        index = 0
        results = []
        with allure.step(title):
            for arg in args:
                index += 1
                "断言形式"
                method = arg[0]
                "实际结果/子集/实际值"
                practical = arg[1]
                "预期结果/父集/比较值"
                expected = arg[2]
                if method == 'eq':
                    if expected is None:
                        result = practical is None
                    else:
                        result = expected == practical
                    allure.attach(json.dumps(f"预期结果: {expected},实际结果: {practical}", ensure_ascii=False, indent=2),
                                  f"第{index}个or断言[相等]: {result}", allure.attachment_type.JSON)
                if method == 'not_eq':
                    if expected is None:
                        result = practical is not None
                    else:
                        result = expected != practical
                    allure.attach(json.dumps(f"预期不相等: {expected},实际结果: {practical}", ensure_ascii=False, indent=2),
                                  f"第{index}个or断言[不相等]: {result}", allure.attachment_type.JSON)
                if method == 'include':
                    result = practical in expected
                    allure.attach(json.dumps(f"子集: {practical},父集: {expected}", ensure_ascii=False, indent=2),
                                  f"第{index}个or断言[包含]: {result}", allure.attachment_type.JSON)
                if method == 'not_include':
                    result = practical not in expected
                    allure.attach(json.dumps(f"子集: {practical},父集: {expected}", ensure_ascii=False, indent=2),
                                  f"第{index}个or断言[不包含]: {result}", allure.attachment_type.JSON)
                if method == 'ge':
                    result = practical >= expected
                    allure.attach(json.dumps(f"实际结果: {practical},比较值: {expected}", ensure_ascii=False, indent=2),
                                  f"第{index}个断言[大于等于]: {result}", allure.attachment_type.JSON)
                if method == 'gt':
                    result = practical > expected
                    allure.attach(json.dumps(f"实际结果: {practical},比较值: {expected}", ensure_ascii=False, indent=2),
                                  f"第{index}个断言[大于]: {result}", allure.attachment_type.JSON)
                if method == 'le':
                    result = practical <= expected
                    allure.attach(json.dumps(f"实际结果: {practical},比较值: {expected}", ensure_ascii=False, indent=2),
                                  f"第{index}个断言[小于等于]: {result}", allure.attachment_type.JSON)
                if method == 'lt':
                    result = practical < expected
                    allure.attach(json.dumps(f"实际结果: {practical},比较值: {expected}", ensure_ascii=False, indent=2),
                                  f"第{index}个断言[小于]: {result}", allure.attachment_type.JSON)
                results.append(result)
                if result:
                    break
            rs = True in results
            assert rs
            return rs

    def delete_all_cookie(self):
        """清除所有cookie"""
        log.info('清除所有cookie')
        self.driver.delete_all_cookies()

    def get_cookie(self, name):
        log.info(f'获取cookie：{name}')
        return self.driver.get_cookie(name)

    def get_cookies(self):
        log.info('获取所有cookie')
        return self.driver.get_cookies()

    def set_cookie(self, cookie: dict):
        log.info(f'添加cookie=》{cookie}')
        self.driver.add_cookie(cookie)

    def add_member_imymac_cookie(self):
        """添加member_imymac的cookie"""
        cookie = Element('User/cookie')
        self.set_cookie(cookie.data)

    @staticmethod
    def update_member_imymac_cookie(data: dict):
        """修改yaml文件中的cookie"""
        cookie = Element('User/cookie')
        cookie.update_data(data, cookie.data)

    def get_windows_handles(self):
        """获取当前窗口的所有句柄"""
        handles = self.driver.window_handles
        log.info(f'获取到窗口所有句柄：{handles}')
        return handles

    def switch_window_by_name(self, handle):
        """
        切换句柄
        :param handle: 句柄名
        :return:
        """
        log.info(f'切换到窗口句柄：{handle}')
        self.driver.switch_to.window(handle)

    def get_window_handle(self):
        """获取当前窗口句柄"""
        handle = self.driver.current_window_handle
        log.info(f'当前窗口句柄{handle}')
        return handle

    def close_driver_page(self):
        """关闭当前窗口标签页"""
        handle = self.get_window_handle()
        self.driver.close()
        log.info(f'关闭当前窗口:{handle}')

    # def click_sale_off_link(self):
    #     """关闭黑色星期五链接"""
    #     log.info('关闭黑色星期五优惠链接')
    #     self.jsInDriver("document.querySelector('div.close-tag').click()")
