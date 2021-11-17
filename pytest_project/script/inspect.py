import os
import yaml
from pytest_project.config.conf import cm
from pytest_project.utils.times import running_time


@running_time
def inspect_element():
    '''
    检查所有的元素是否正确
    只能做一个简单的检查
    :return:
    '''

    for flies in os.listdir(cm.ELEMENT_DIR):
        _path = os.path.join(cm.ELEMENT_DIR, flies)
        with open(_path, encoding='utf-8') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
        for k in data.values():
            try:
                pattern, value = k.split('=')
            except ValueError:
                raise Exception('元素表达式没有=')
            if pattern not in cm.LOCATE_MODE:
                raise Exception('%s中的元素[%s]没有指定类型不是设置中的' % (_path, k))
            if pattern == 'xpath':
                assert '//' in value, '%s中元素[%s] xpath类型与值不匹配' % (_path, k)


if __name__ == '__main__':
    inspect_element()
