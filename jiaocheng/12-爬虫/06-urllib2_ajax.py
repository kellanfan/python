#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Mon 01 Apr 2019 08:40:08 AM CST

# File Name: 06-urllib2_ajax.py
# Description: 爬取豆瓣排行，模拟post请求

"""

import urllib
import urllib2

url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"}

formdata = {
    "start": "0",
    "limit": "20"
}

data = urllib.urlencode(formdata)

request = urllib2.Request(url, data=data, headers=headers)
jdata = urllib2.urlopen(request).read()
print jdata
