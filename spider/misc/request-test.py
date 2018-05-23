#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Mon 10 Jul 2017 01:49:51 PM CST

# File Name: request-test.py
# Description:

"""

import requests, json
#from bs4 import BeautifulSoup

#url = raw_input("input your url: ")
url = 'http://python.org'
if 'http' not in url:
    url = 'http://' + url
headers = {
    'user-agent': ('Mozilla/5.0 (Windows NT 6.2; WOW64)'
                       'AppleWebKit/537.36 (KHTML, like Gecko)'
                       'Chrome/56.0.2924.87 Safari/537.36'),
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
}
req = requests.get(url, headers=headers)
print req.status_code
if 'Python' in req.content:
    print "hahahaha"
print "======================"
pload = dict(aa='11', bb='22')
req1 = requests.post("http://httpbin.org/post", data=pload)
print req1.text


print "======================"

