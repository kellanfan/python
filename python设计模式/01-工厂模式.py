#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Sun 22 Jul 2018 10:44:24 PM CST

# File Name: 01-工厂模式.py
# Description: 模拟工厂模式，对不同的存储信息方式进行解析，并返回一个字典

"""
import yaml, json
import sys


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

def connect_factory(filepath):
    if filepath.endswith('.yaml'):
        connector = YamlConnector(filepath)
    elif filepath.endswith('.json'):
        connector = JsonConnector(filepath)
    else:
        raise ValueError('cannot connect to {}'.format(filename))
    return connector

def connect_to(filepath):
    factory = None
    try:
        factory = connect_factory(filepath)
    except ValueError as e:
        print(e)
    return factory

def usage():
    print('''
    Usage:
        %s filename
            '''%sys.argv[0])

def main():
    if len(sys.argv) == 2:
        filepath = sys.argv[1]
    else:
        usage()
        sys.exit(-1)

    factory = connect_to(filepath)
    print(factory.datainfo)


if __name__ == '__main__':
    main()
