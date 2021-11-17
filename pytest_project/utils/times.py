import time
import datetime
from functools import wraps


def timestamp():
    '''
    时间戳
    :return:
    '''
    return time.time()


def datetime_format(fmt='%Y年%m月%d日-%H时%M分%S秒'):
    '''
    格式日期
    :param fmt: 默认格式
    :return:
    '''
    return datetime.datetime.now().strftime(fmt)


def sleep(seconds=1.0):
    '''
    暂停
    :param seconds: 默认一秒钟
    :return:
    '''
    return time.sleep(seconds)


def running_time(func):
    '''
    函数启动时间装饰器
    :param func:
    :return:
    '''

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = timestamp()
        res = func(*args, **kwargs)
        print('效验元素用时：%.3f' % (timestamp() - start))
        return res

    return wrapper


if __name__ == '__main__':
    now = datetime_format()
    print(now)
