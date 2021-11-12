import os

download_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'download-dir')


def clear_download_files():
    for i in os.listdir(download_dir):
        os.remove(download_dir + os.sep + i)


clear_download_files()
