import os
from pytest_project.utils.logger import Log
import time

from pytest_project.config.conf import cm


class Clear(object):
    download_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'download-dir')
    log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logs')

    def clear_download_files(self):
        for i in os.listdir(self.download_dir):
            if i == '__init__.py':
                continue
            else:
                try:
                    os.remove(self.download_dir + os.sep + i)
                except PermissionError:
                    time.sleep(5)
                    try:
                        os.remove(self.download_dir + os.sep + i)
                    except PermissionError:
                        Log().get_log().error('清空下载文件夹失败，手动清空')
                    except FileNotFoundError:
                        Log().get_log().error('文件已被其他线程清除')

    def clear_log_file(self):
        for i in os.listdir(self.log_dir):
            if i == cm.log_file.split(os.sep)[-1]:
                break
            else:
                os.remove(self.log_dir + os.sep + i)


clear = Clear()
# clear.clear_download_files()
clear.clear_log_file()
