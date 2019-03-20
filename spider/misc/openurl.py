#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Thu 26 Apr 2018 08:04:30 PM CST

# File Name: openurl.py
# Description:

"""
import sys
import random
import requests
from fake_useragent import UserAgent

class OpenUrl(object):
    def __init__(self, url, encode = 'utf-8'):
        self.__url = url
        self.ua = UserAgent(verify_ssl=False)
        self.__headers = {
              'User-Agent': self.ua.random,
              'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
              'connection': 'keep-alive',
        }
        self.__encode = encode
        self.__session = requests.Session()
        self.__cookie = None

    def openurl(self):
        try:
            requests.adapters.DEFAULT_RETRIES = 10
            response = requests.get(self.__url, headers=self.__headers)
            response.encoding = self.__encode
            return response.status_code, response.text
        except:
            return 400, None

if __name__ == '__main__':
    url = input("请输入url：")
    encode = input("请输入编码格式<utf-8(default)/gb2312...>: ")
    if encode == '':
        ourl = OpenUrl(url)
    else:
        if encode in ['gb2312', 'gbk']:
            ourl = OpenUrl(url, encode)
        else:
            print("傻逼么？不是告诉你了么？！")
            sys.exit(1)
    print(ourl.openurl()[1])
