#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Wed 27 Jun 2018 04:09:18 PM CST

# File Name: 02-redis.py
# Description:

"""

from redis import *

class RedisHelper(object):
    def __init__(self,host='localhost',port='6379'):
        self.__host = host
        self.__port = port
        self.__r = Redis(self.__host, self.__port)

    def set(self,key,value):
        self.__r.set(key, value)

    def get(self,key):
        return self.__r.get(key)

if __name__ == '__main__':
    r = RedisHelper()
    r.set('haha1','12312341')
    print(r.get('haha1'))
