#/usr/bin/env python
#coding=utf-8
"""
# Author: kellanfan
# Created Time : Wed 25 Apr 2018 11:43:21 PM CST

# File Name: meijutiantang.py
# Description:

"""
import requests
import re
import os


def open_url(url):  
    headers = {
              'user-agent': ('Mozilla/5.0 (Windows NT 6.2; WOW64)'
                               'AppleWebKit/537.36 (KHTML, like Gecko)'
                               'Chrome/56.0.2924.87 Safari/537.36'),
              'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    }
    response = requests.get(url, headers=headers)
    #原页面为gb2312，需要指定requests对象encoding值
    response.encoding = 'gb2312'
    return response.status_code, response.text

def save_text(url_id, link_list):
    file_name = './meiju/%s.txt'%url_id
    f = open(file_name, 'w+')
    for link in link_list:
        f.write(link + '\n')
    f.close()
    
#构建url
url_header = 'http://www.meijutt.com/content/meiju'
url_end = '.html'
reg = re.compile(r'<a href="(ed2k://\|file\|.+?)">') #加？非贪婪
if not os.path.exists('./meiju'):
    os.mkdir('./meiju')

for url_id in range(10000, 50000):
    url = url_header + str(url_id)  + url_end
    status, html = open_url(url)
    if status == 200:
        link_list = re.findall(reg, html)
        save_text(url_id, link_list)
