#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Thu 26 Apr 2018 08:04:30 PM CST

# File Name: openurl.py
# Description:

"""

import requests

class OpenUrl(object):
    def __init__(self, url, encode = 'utf-8'):
        self.__url = url
        self.__headers = {
              'user-agent': ('Mozilla/5.0 (Windows NT 6.2; WOW64)'
                               'AppleWebKit/537.36 (KHTML, like Gecko)'
                               'Chrome/56.0.2924.87 Safari/537.36'),
              'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
              'Connection': 'close'
        }
        self.__encode = encode

    def openurl(self):
        try:
            requests.adapters.DEFAULT_RETRIES = 10
            response = requests.get(self.__url, headers=self.__headers)
            response.encoding = self.__encode
            return response.status_code, response.text
        except:
            status_code = 400
            text = None
            return status_code, text

if __name__ == '__main__':
    url = 'http://www.meijutt.com/content/meiju23030.html'
    ourl = OpenUrl(url,'gb2312')
    print(ourl.openurl())
