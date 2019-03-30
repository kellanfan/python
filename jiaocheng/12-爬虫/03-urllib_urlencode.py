#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Wed 27 Mar 2019 08:31:03 AM CST

# File Name: 03-urllib_urlencode.py
# Description:
    urllib仅可以接受url，不能创建设置了headers的Request类实例
    urllib提供了urlencode方法来GET查询字符串的产生，而urllib2没有
    所以这2个经常共用
"""

import urllib
import urllib2
url = "http://www.baidu.com/s"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"}

keyword = raw_input("请输入关键词: ")
wd = urllib.urlencode({"wd":keyword})
fullurl = url + '?' + wd
request = urllib2.Request(fullurl, headers=headers)
response = urllib2.urlopen(request)

print response.read()
