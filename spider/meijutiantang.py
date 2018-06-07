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
from misc import openurl
from misc import mysql_connect

def logger(code, msg):
    '''记录日志'''
    logging.basicConfig(filename='/root/data/meiju/meiju.log',level=logging.INFO,format='%(asctime)s %(levelname)s: %(message)s')
    if code == 200:
        message = 'get data from [%s] successful!!!' %msg
        logging.info(message)
    else:
        message = 'get data from [%s] failed!!!' %msg
        logging.error(message)

def save_text(url_id, title, link_list):
    file_name = '/root/data/meiju/%s.txt'%url_id
    f = open(file_name, 'w+')
    f.write(title + '\n')
    for link in link_list:
        f.write(link + '\n')
    f.close()
    
def send_mysql(name, str_down):
    sql = "insert into meiju(name, content) value ('%s', '%s')"%(name,str_down)
    connect = mysql_connect.MysqlConnect('./misc/mysql_data.yaml')
    code = connect.change_data('spiderdata', sql)
    if code == 0:
        print('%s ok'%name)
    else:
        print('%s error, message: %s'%(name,code))

def main():
    #构建url
    url_header = 'http://www.meijutt.com/content/meiju'
    url_end = '.html'
    text_reg = re.compile(r'<a href="(ed2k://\|file\|.+?)">') #加？非贪婪
    
    #if not os.path.exists('/root/data/meiju'):
    #    os.mkdir('/root/data/meiju')

    for url_id in range(20000, 23600):
        url = url_header + str(url_id)  + url_end
        ourl = openurl.OpenUrl(url, 'gb2312')
        status, html = ourl.openurl()
        logger(status, url)
        if status == 200:
            link_list = re.findall(text_reg, html)
            if link_list != []:
                str_down = '#'.join(link_list)
            
            try:
                name = re.search('<title>(.+?)迅雷下载',html).group(1)
            except:
                name = "None"
            else:
                send_mysql(name, str_down)
        time.sleep(0.5)

if __name__ == '__main__':
    main()
