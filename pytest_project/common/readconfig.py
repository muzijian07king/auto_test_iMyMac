import configparser
from pytest_project.config.conf import cm

HOST = 'HOST'


class ReadConfig(object):
    '''
    配置文件
    读取ini文件
    '''

    def __init__(self):
        self.config = configparser.RawConfigParser()  # 当有%的符号时请使用Raw读取
        self.config.read(cm.ini_file, encoding='UTF-8')

    def _get(self, section, option):
        '''
        获取配置文件
        :param section: 节点
        :param option: 节点中的key,类似字典的key
        :return:
        '''
        return self.config.get(section, option)

    def _set(self, section, option, value):
        '''
        修改配置文件的节点值
        :param section: 节点
        :param option: 节点中的key
        :param value: 修改的value值
        :return:
        '''
        self.config.set(section, option, value)
        with open(cm.ini_file, 'w') as f:
            self.config.write(f)

    def _getAll(self, section):
        '''
        获取节点的所有key value
        :param section:节点
        :return:返回列表
        '''
        return self.config.items(section)

    @property
    def url(self):
        return self._get(HOST, 'imymac')

    def get_url(self, host):
        return self._get(HOST, host)

    @property
    def get_url_all(self):
        return self._getAll(HOST)


'''
饿汉式
'''
ini = ReadConfig()

if __name__ == '__main__':
    # list_url = ini.get_url_all
    # for i in range(len(list_url)):
    #     for j in range(len(list_url[0])):
    #         print(list_url[i][j])

    print(ini.get_url('pdf-compressor'))
