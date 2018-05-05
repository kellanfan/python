#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Thu 26 Apr 2018 08:04:30 PM CST

# File Name: openurl.py
# Description:

"""

import requests
def open_url(url, encode):  
    headers = {
              'user-agent': ('Mozilla/5.0 (Windows NT 6.2; WOW64)'
                               'AppleWebKit/537.36 (KHTML, like Gecko)'
                               'Chrome/56.0.2924.87 Safari/537.36'),
              'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    }
    response = requests.get(url, headers=headers)
    #原页面为gb2312，需要指定requests对象encoding值
    response.encoding = encode
    return response.status_code, response.text

if __name__ == '__main__':
    #url = 'http://www.runningman-fan.com/180429-zz.html'
    url = 'https://www.piaohua.com/html/kehuan/2018/0502/33625.html'
    print(open_url(url,'utf-8'))
