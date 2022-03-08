import zipfile
from pathlib2 import Path


def compress_dir(compress_path, path_zip):
    """
    压缩文件夹下的所有文件
    :param compress_path:需要压缩的路径
    :param path_zip:压缩指定路径+压缩名
    :return:
    """
    try:
        # 返回路径下所有文件路径
        file_list = list(Path(compress_path).glob("**/*"))
        with zipfile.ZipFile(path_zip, 'w') as z:
            for f in file_list:
                # str(f)[len(compress_path):] 压缩文件名
                z.write(f, str(f)[len(compress_path):])
    except Exception:
        raise print('压缩失败')


if __name__ == '__main__':
    import sys
    sys.path.append(Path.cwd().parent)
