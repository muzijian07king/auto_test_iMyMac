import os
from config.conf import cm


class Clear(object):
    download_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'download-dir')
    log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logs')

    def clear_download_files(self):
        for i in os.listdir(self.download_dir):
            if i == '__init__.py':
                break
            else:
                os.remove(self.download_dir + os.sep + i)

    def clear_log_file(self):
        for i in os.listdir(self.log_dir):
            if i == cm.log_file.split(os.sep)[-1]:
                break
            else:
                os.remove(self.log_dir + os.sep + i)


clear = Clear()
clear.clear_download_files()
clear.clear_log_file()
