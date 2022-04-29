import logging
from pytest_project.config.conf import cm


class Log:
    def __init__(self):
        self.logger = logging.getLogger()
        if not self.logger.handlers:
            self.logger.setLevel(logging.INFO)

            # 创建一个handle写入文件
            file_handle = logging.FileHandler(cm.log_file, encoding='utf-8')
            file_handle.setLevel(logging.INFO)

            # 创建一个handle输出到控制台
            console_handle = logging.StreamHandler()
            console_handle.setLevel(logging.INFO)

            # 定义输出的格式
            formatter = logging.Formatter(self.format_log)
            file_handle.setFormatter(formatter)
            console_handle.setFormatter(formatter)

            # 创建的handle添加到容器中
            self.logger.addHandler(file_handle)
            self.logger.addHandler(console_handle)

    def get_log(self):
        return self.logger

    @property
    def format_log(self):
        return '%(levelname)s\t%(asctime)s\t[%(filename)s:%(lineno)d]\t%(message)s'
