import os
import sys
from selenium.webdriver.common.by import By
import datetime


class ConfigManager(object):
    """
    固定参数
    """

    # pytest_project绝对路径
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # xlsx目录
    XLSX_DIR = os.path.join(BASE_DIR, 'excel_data')

    # 页面元素目录
    ELEMENT_DIR = os.path.join(BASE_DIR, 'page_element')

    # 报告文件文件夹路径
    REPORT_DIR = os.path.join(BASE_DIR, 'report')
    REPORT_COMPRESS_FILE = os.path.join(REPORT_DIR, 'report.zip')

    # 浏览器下载文件默认地址
    download_dir = os.path.join(BASE_DIR, 'download-dir')

    # 非图片文件
    not_image = os.path.join(BASE_DIR, 'pytest.ini')

    # 最新报告文件路径方法
    def get_report_file(self):
        list_name = os.listdir(self.REPORT_DIR)
        list_name.sort(key=lambda fn: os.path.getmtime(os.path.join(self.REPORT_DIR, fn)))
        latest_report = os.path.join(self.REPORT_DIR, list_name[-1])
        return latest_report

    # 获取浏览器默认下载路径最新文件的后缀名
    def get_download_filename(self):
        list_name = os.listdir(self.download_dir)
        list_name.sort(key=lambda fn: os.path.getmtime(os.path.join(self.download_dir, fn)))
        return list_name[-1].split('.')[-1]

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

    Photo = os.path.join(BASE_DIR, 'photo.png')

    # 日志文件
    @property
    def log_file(self):
        """
        只读属性
        :return: 日志文件路径
        """
        log_dir = os.path.join(self.BASE_DIR, 'logs')
        if not os.path.exists(log_dir):
            os.mkdir(log_dir)
        return os.path.join(log_dir, '{}.log'.format(datetime.datetime.now().strftime('%Y年%m月%d日')))

    # ini配置文件
    @property
    def ini_file(self):
        ini_file = os.path.join(self.BASE_DIR, 'config', 'config.ini')
        if not os.path.exists(ini_file):
            raise FileExistsError('配置文件%s不存在' % ini_file)
        return ini_file

    @property
    def VPN_Switch(self):
        return sys.platform.startswith('linux')


cm = ConfigManager()
