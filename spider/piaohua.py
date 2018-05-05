#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Sat 05 May 2018 09:57:24 AM CST

# File Name: piaohua.py
# Description: 爬取飘花网的电影资源

"""
import re
import time
from openurl import open_url
def get_url():
    main_url = 'https://www.piaohua.com/html/kehuan/index.html'
    code,main_content = open_url(main_url, 'utf-8')
    pages = re.search("共 <strong>(\d+)</strong>页", main_content).group(1)
    reg = re.compile(r'<a href="(/html/kehuan/.+?)"')
    f = open('url_list.txt','w')
    for page in range(1,int(pages)):
        list_url = 'https://www.piaohua.com/html/kehuan/list_%d.html' %page
        sub_code,sub_content = open_url(list_url, 'utf-8')
        if sub_code == 200:
            ll = re.findall(reg, sub_content)
            print(ll)
            for l in list(set(ll)):
                f.write(l+'\n')
        time.sleep(0.5)
    f.close()

def get_download_url(file):
    f = open(file)
    fd = open('down_url.txt','w')
    reg = re.compile(r'<a href="(magnet:\?.+?)\r">')
    for line in f.readlines():
        line = line.split('\n')[0]
        url = 'https://www.piaohua.com' + line
        code, content = open_url(url, 'utf-8')
        list_down = []
        if code == 200:
            time.sleep(0.5)
            name = re.search("<title>(.+?)下载",content).group(1)
            list_down = re.findall(reg, content)
            if list_down != []:
                fd.write(name + '#####\n')
                for down in list_down:
                    fd.write(down+'\t')
                fd.write('')
    f.close()
    fd.close()

if __name__ == '__main__':
    get_download_url('url_list.txt')
