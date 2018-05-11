#/usr/bin/env python
#coding=utf-8
"""
# Author: kellanfan
# Created Time : Wed 25 Apr 2018 11:43:21 PM CST

# File Name: meijutiantang.py
# Description:

"""
import re
import os
import time
import logging
from openurl import OpenUrl


def save_text(url_id, title, link_list):
    file_name = '/root/data/meiju/%s.txt'%url_id
    f = open(file_name, 'w+')
    f.write(title + '\n')
    for link in link_list:
        f.write(link + '\n')
    f.close()
    
def main():
    #构建url
    url_header = 'http://www.meijutt.com/content/meiju'
    url_end = '.html'
    text_reg = re.compile(r'<a href="(ed2k://\|file\|.+?)">') #加？非贪婪
    
    if not os.path.exists('/root/data/meiju'):
        os.mkdir('/root/data/meiju')

    for url_id in range(10000, 40000):
        url = url_header + str(url_id)  + url_end
        ourl = OpenUrl(url, 'gb2312')
        status, html = ourl.openurl()
        if status == 200:
            link_list = re.findall(text_reg, html)
            name = re.search('<title>(.+?)迅雷下载',html).group(1)
            save_text(url_id, name, link_list)
        time.sleep(0.5)

if __name__ == '__main__':
    main()
