import os
from config.conf import cm

download_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'download-dir')
log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logs')


def clear_download_files():
    for i in os.listdir(download_dir):
        if i == '__init__.py':
            break
        else:
            os.remove(download_dir + os.sep + i)


def clear_log_file():
    for i in os.listdir(log_dir):
        if i == cm.log_file.split(os.sep)[-1]:
            break
        else:
            os.remove(log_dir + os.sep + i)


clear_download_files()
clear_log_file()