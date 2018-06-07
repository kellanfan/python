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
from misc import mysql_connect
from misc import openurl

def get_url():
    main_url = 'https://www.piaohua.com/html/lianxuju/index.html'
    ourl = openurl.OpenUrl(main_url)
    code,main_content = ourl.openurl()
    pages = re.search("共 <strong>(\d+)</strong>页", main_content).group(1)
    reg = re.compile(r'<a href="(/html/lianxuju/.+?)"')
    f = open('url_list.txt','w')
    for page in range(1,int(pages)):
        list_url = 'https://www.piaohua.com/html/lianxuju/list_%d.html' %page
        sub_ourl = OpenUrl(list_url)
        sub_code,sub_content = sub_ourl.openurl()
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
    reg = re.compile(r'<a href="(ftp:.+?)">')
    #reg = re.compile(r'<a href="(magnet:.+?)">')
    for line in f.readlines():
        line = line.split('\n')[0]
        url = 'https://www.piaohua.com' + line
        ourl = openurl.OpenUrl(url)
        code, content = ourl.openurl()
        list_down = []
        if code == 200:
            time.sleep(0.5)
            name = re.search("<title>(.+?)下载",content).group(1)
            list_down = re.findall(reg, content)
            if list_down != []:
                str_down = '#'.join(list_down)
                send_mysql(name, str_down)

def send_mysql(name, str_down):
    sql = "insert into piaohua(name, content) value ('%s', '%s')"%(name,str_down)
    connect = mysql_connect.MysqlConnect('./misc/mysql_data.yaml')
    code = connect.change_data('spiderdata', sql)
    if code == 0:
        print('%s ok'%name)
    else:
        print('%s error,message: %s'%(name, code))


if __name__ == '__main__':
    #get_url()
    get_download_url('url_list.txt')
