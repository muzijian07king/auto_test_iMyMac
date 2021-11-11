import os
from pytest_project.config.conf import cm


def clear_download_files():
    for i in os.listdir(cm.download_dir):
        os.remove(cm.download_dir + os.sep + i)


clear_download_files()
