# pylint: disable=no-member
# -*- encoding: utf-8 -*-
'''
@File    :   03-工厂模式简化版.py
@Time    :   2019/10/16 22:39:05
@Author  :   Kellan Fan 
@Version :   1.0
@Contact :   kellanfan1989@gmail.com
@Desc    :   禁止直接实例化一个类的简洁方式
'''

# here put the import lib
import yaml, json
import sys
class Connector(object):
    class YamlConnector(object):
        def __init__(self, filepath):
            with open(filepath) as f:
                self.data = yaml.load(f)
        @property
        def datainfo(self):
            return self.data

    class JsonConnector(object):
        def __init__(self, filepath):
            self.data = dict()
            with open(filepath) as f:
                self.data = json.load(f)
        @property
        def datainfo(self):
            return self.data
    def bulid_connector(self,filepath):
        if filepath.endswith('.yaml'):
            connector = self.YamlConnector(filepath)
        elif filepath.endswith('.json'):
            connector = self.JsonConnector(filepath)
        else:
            raise ValueError('cannot connect to {}'.format(filepath))
        return connector

def connect_to(filepath):
    factory = Connector()
    try:
        factory = factory.bulid_connector(filepath)
    except ValueError as e:
        print(e)
    return factory

def usage():
    print('''
    Usage:
        {} filename
            '''.format(sys.argv[0]))

def main():
    if len(sys.argv) == 2:
        filepath = sys.argv[1]
    else:
        usage()
        sys.exit()

    factory = connect_to(filepath)
    print(factory.datainfo)


if __name__ == '__main__':
    main()