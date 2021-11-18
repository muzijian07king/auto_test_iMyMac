import os
from builtins import isinstance
import yaml
from pytest_project.config.conf import cm
from pathlib import Path


class Element(object):
    '''
    获取元素
    读取yaml文件
    '''

    def __init__(self, name):
        """
        读取yaml位置以及内容
        :param name:
        """
        self.file_name = '%s.yaml' % name
        self.element_path = cm.ELEMENT_DIR / Path(self.file_name)
        if not os.path.exists(self.element_path):
            raise FileExistsError('%s 文件不存在' % self.element_path)
        with open(self.element_path, encoding='utf-8') as f:
            self.data = yaml.load(f, Loader=yaml.FullLoader)

    def __getitem__(self, item):
        """数据层数为1，获取value"""
        item_data = self.data.get(item)
        if item_data:
            name, value = item_data.split('=', 1)
            return name, value
        raise ArithmeticError('{}中不存在关键字：{}'.format(self.file_name, item))

    def getLanguage(self, name):
        """根据缩写获取语言名称"""
        return self.data.get(name)


def get_any_key_info(key_name="", yaml_data=None):
    """递归获取多重嵌套yaml储存的value"""
    # for循环字典这一层的所有key值
    for i in yaml_data.keys():
        # 如果当前的key是我们要找的
        if i == key_name:
            ele_key, ele_value = yaml_data[i].split('=', 1)
            return ele_key, ele_value
        # 如果当前的key不是我们找的key，并且是字典类型
        elif type(yaml_data[i]) == dict:
            # 使用递归方法，查找下一层的字典
            # 每层递归要返回一个值
            value = get_any_key_info(key_name, yaml_data[i])
            # 显示检查，以防提前跳过
            if value is not None:
                return value


class get_recursion_key(object):
    def __init__(self):
        self.keys = []

    def get_recursion_key(self, datas):
        """递归获取所有的键值对的key"""
        for self.key, self.value in datas.items():
            """获取循环总次数"""
            if type(self.value) == dict:
                """遇到value为字典类型就递归下去"""
                recursion = self.get_recursion_key(self.value)
                """获取所有key所以待递归为None时就返回数据"""
                if recursion is None:
                    return recursion
            else:
                self.keys.append(self.key)
        return self.keys


class get_root_all_value(object):

    def __init__(self):
        self.list_root = []

    def get_root_all_value(self, datas):
        """
        获取根节点下所有的value
        :param datas: 传入字典
        :return: 返回列表
        """
        for self.value in datas.values():
            if type(self.value) == dict:
                values = self.get_root_all_value(self.value)
                if self.value is None:
                    return values
            else:
                k, v = self.value.split('=', 1)
                self.list_root.append((k, v))
        return self.list_root


class get_branch_all_value(object):

    def __init__(self):
        self.list_branch = []

    def get_branch_all_value(self, datas, name=''):
        """
        获取某个节点下的所有value默认根节点
        :param datas: 传入字典
        :param name: 节点名称
        :return: 数据列表
        """
        if name == '':
            return get_root_all_value().get_root_all_value(datas)
        else:
            if hasattr(datas.get(name), 'items'):
                for key, value in datas.get(name).items():
                    if type(value) == dict:
                        values = self.get_branch_all_value(value, list(value.keys())[0])
                        if value is None:
                            return values
                    else:
                        tuple_key, tuple_value = value.split('=', 1)
                        self.list_branch.append((tuple_key, tuple_value))
            else:
                tuple_1, tuple_2 = get_any_key_info(name, datas)
                self.list_branch.append((tuple_1, tuple_2))
            return self.list_branch


class get_branch_all_keys(object):
    def __init__(self):
        self.list_keys = []

    def get_branch_all_keys(self, datas=None, name=''):
        """
        获取某个节点下的所有key默认根节点(只能获取某个节点下的所有key)
        :param datas: 传入字典
        :param name: 节点名称
        :return: 数据列表
        """
        if name == '':
            return get_recursion_key().get_recursion_key(datas)
        else:
            if hasattr(datas.get(name), 'items'):
                for self.key, self.value in datas.get(name).items():
                    if type(self.value) == dict:
                        values = self.get_branch_all_keys(self.value, list(self.value.keys())[0])
                        if self.value is None:
                            return values
                    else:
                        self.list_keys.append(self.key)
            else:
                for i in get_recursion_key().get_recursion_key(datas):
                    self.list_keys.append(i)
            return self.list_keys


list_value = []


class get_values_in_name(object):
    """
    根据name获取所有的value
    """

    def __init__(self):
        list_value.clear()

    def get_values_in_name(self, data, name):
        # for循环字典这一层的所有key值
        for i in data.keys():
            # 如果当前的key是我们要找的
            if i == name:
                k, v = data[i].split('=', 1)
                list_value.append((k, v))
            # 如果当前的key不是我们找的key，并且是字典类型
            if type(data[i]) == dict:
                # 使用递归方法，查找下一层的字典
                # 每层递归要返回一个值
                value = self.get_values_in_name(data[i], name)
                # 显示检查，以防提前跳过
                if value is None:
                    return value
        return list_value


def get_branch_value_with_key(key, data, branch=None):
    """
    获取某个节点下的某一个元素的值
    :param key: 元素key
    :param data:yaml数据
    :param branch: 节点名 默认为空
    :return:key对应的值
    """
    if branch is None:
        "判断节点是否为空"
        return data[key]
    elif isinstance(data[branch], dict):
        for i in data[branch].keys():
            "遍历该节点下的所有key"
            if i == key:
                return tuple(data[branch][i].split('=', 1))
            elif type(data[branch][i]) == dict:
                "key对应的value是字典就递归"
                value = get_branch_value_with_key(key, data[branch], i)
                if value is not None:
                    return value


if __name__ == '__main__':
    body = Element('Store/body')
    print(body['price'])
    # print(body['cancelCouponButton'])
    # print(get_branch_all_keys().get_branch_all_keys(sitemap.data, 'Company'))
    # print(get_branch_all_keys().get_branch_all_keys(sitemap.data, 'Products'))
    # print(get_branch_all_keys().get_branch_all_keys(sitemap.data, 'Help'))
    # print(get_branch_all_keys().get_branch_all_keys(sitemap.data, 'More'))
    # # print(get_recursion_key(foot.data))
    # print(get_branch_value_with_key('PowerMyMac', sitemap.data, 'More'))
    # # print(foot['Youtube'])
    # # print(get_branch_all_value(foot.data))
    # # print(get_recursion_key(foot.data))
    # print(get_branch_all_keys().get_branch_all_keys(foot.data, 'Language'))
    # keys.clear()
    # language = Element('PowerMyMac/browser-duplicate')
    # print(language['carousel-comment-class'])
