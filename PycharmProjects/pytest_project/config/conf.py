import os
from selenium.webdriver.common.by import By
from pytest_project.utils.times import datetime_format


class ConfigManager(object):
    '''
    固定参数
    '''

    # pytest_project绝对路径
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # xlsx目录
    XLSX_DIR = os.path.join(BASE_DIR, 'excel_data')

    # 页面元素目录
    ELEMENT_DIR = os.path.join(BASE_DIR, 'page_element')

    # 报告文件文件夹路径
    REPORT_DIR = os.path.join(BASE_DIR, 'report'+os.sep+'pytest_html')

    # 浏览器下载文件默认地址
    download_dir = os.path.join(BASE_DIR, 'download-dir')

    # 最新报告文件路径方法
    def get_report_file(self):
        list = os.listdir(self.REPORT_DIR)
        list.sort(key=lambda fn: os.path.getmtime(os.path.join(self.REPORT_DIR, fn)))
        latest_report = os.path.join(self.REPORT_DIR, list[-1])
        return latest_report

    # 获取浏览器默认下载路径最新文件的后缀名
    def get_download_filename(self):
        list = os.listdir(self.download_dir)
        list.sort(key=lambda fn: os.path.getmtime(os.path.join(self.download_dir, fn)))
        return list[-1].split('.')[-1]

    # 元素定位元素的类型
    LOCATE_MODE = {
        'css': By.CSS_SELECTOR,
        'id': By.ID,
        'name': By.NAME,
        'class': By.CLASS_NAME,
        'link': By.LINK_TEXT,
        'xpath': By.XPATH,
        'tag': By.TAG_NAME
    }

    # 邮件信息
    EMAIL_INFO = {
        'user_email': 'muzijian07king@163.com',
        'password': 'XERVFELLOWCZOJZH',
        'smtp_host': 'smtp.163.com',
        'smtp_port': 465
    }

    # 收件人
    ADDRESSEE = [
        'muzijian07king@163.com', '1325282680@qq.com'
    ]

    # 日志文件
    @property
    def log_file(self):
        '''
        只读属性
        :return: 日志文件路径
        '''
        log_dir = os.path.join(self.BASE_DIR, 'logs')
        if not os.path.exists(log_dir):
            os.mkdir(log_dir)
        return os.path.join(log_dir, '{}.log'.format(datetime_format(fmt='%Y年%m月%d日')))

    # ini配置文件
    @property
    def ini_file(self):
        ini_file = os.path.join(self.BASE_DIR, 'config', 'config.ini')
        if not os.path.exists(ini_file):
            raise FileExistsError('配置文件%s不存在' % ini_file)
        return ini_file

    def screen_path(self):
        '''截图目录'''
        screenshot_dir = os.path.join(self.BASE_DIR, 'screen_capture')
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)
        now_time = datetime_format(fmt='%Y年%m月%d日_%H时%M分%S秒')
        screen_file = os.path.join(screenshot_dir, '{}.png'.format(now_time))
        return now_time, screen_file


cm = ConfigManager()
if __name__ == '__main__':
    print(cm.REPORT_DIR)
