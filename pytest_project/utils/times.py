import time
import datetime
from functools import wraps
from pytest_project.utils.logger import log


def timestamp():
    """
    时间戳
    :return:
    """
    return time.time()


def datetime_format(fmt='%Y年%m月%d日-%H时%M分%S秒'):
    """
    格式日期
    :param fmt: 默认格式
    :return:
    """
    return datetime.datetime.now().strftime(fmt)


def get_utctime(fmt='%Y%m%d%H%M%S'):
    """
    获取世界标准世界
    :param fmt: 默认格式：%Y%m%d%H%M%S
    :return:
    """
    return datetime.datetime.now().utcnow().strftime(fmt)


def sleep(seconds=1.0):
    """
    暂停
    :param seconds: 默认一秒钟
    :return:
    """
    time.sleep(seconds)
    log.debug(f'睡眠{seconds}秒')


def running_time(func):
    """
    函数启动时间装饰器
    :param func:
    :return:
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = timestamp()
        res = func(*args, **kwargs)
        print('效验元素用时：%.3f' % (timestamp() - start))
        return res

    return wrapper


def compare_date(date1, date2, fmt='%b %d,　%Y'):
    """
    比较两时间的差值
    :param date1: 时间1(与格式对应)
    :param date2: 时间2(与格式对应)
    :param fmt:   默认格式%月 %日, %年
    :return:相差天数，date1-date2
    """
    try:
        date1 = datetime.datetime.strptime(date1, fmt)
        date2 = datetime.datetime.strptime(date2, fmt)
    except Exception as e:
        log.error('日期格式错误')
        raise e
    return (date1 - date2).days


if __name__ == '__main__':
    print(compare_date('February 20, 2022', 'Nov 16, 2022'))
