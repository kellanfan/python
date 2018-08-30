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
import sys
#发现re确实不好处理一些特殊的html，改动bs4
from bs4 import BeautifulSoup
from lxml import etree
from misc import mysql_connect
from misc import openurl

def get_url(ftype):
    '''对于这种临时数据暂时存到文件中'''
    main_url = 'https://www.piaohua.com/html/%s/index.html' %ftype
    ourl = openurl.OpenUrl(main_url)
    code,main_content = ourl.openurl()
    if code ==  200:
        #soup = BeautifulSoup(main_content, 'lxml')
        #b = soup.find_all(text=re.compile("共(\d+)页"))[0]
        #pages = re.sub('\D', "", str(b.split('页')[0]))
        selecter = etree.HTML(main_content)
        pages = int(selecter.xpath('//li[@class="end"]/a')[0].attrib['href'].split("_")[1].split('.')[0])
    else:
        print("bad url: %s" %main_url)
        sys.exit(-1)
    fname = 'url_list_' + ftype +'.txt'
    f = open(fname,'w')
    for page in range(1,int(pages)):
        list_url = 'https://www.piaohua.com/html/%s/list_%d.html' %(ftype, page)
        sub_ourl = openurl.OpenUrl(list_url)
        sub_code,sub_content = sub_ourl.openurl()
        if sub_code == 200:
            selector = etree.HTML(sub_content)
            for link in selector.xpath('//span/a'):
                sub_url = link.attrib['href']
                if sub_url.startswith('/html/'+ftype ):
                    f.write(sub_url+'\n')
        time.sleep(0.5)
    f.close()
    time.sleep(1)
    return f

def get_download_url(filename,ftype):
    '''主要函数'''
    #读取文件
    with open(filename) as f:
        for line in f.readlines():
            #读取文件每一行
            line = line.split('\n')[0]
            #构建url
            url = 'https://www.piaohua.com' + line
            #获取html内容
            ourl = openurl.OpenUrl(url)
            code, content = ourl.openurl()
            #初始化list
            list_down = []
            #判断是否正确打开
            if code == 200:
                #反爬虫
                time.sleep(0.5)
                #构建soup
                soup = BeautifulSoup(content,'lxml')
                #获取名称
                name = soup.title.string.split('_')[0]
                #获取a标签的href属性，并去除\r，避免后续处理的麻烦
                for link in soup.find_all('a'):
                    url = link.get('href')
                    if 'ftp' in url:
                        url = ''.join(url.split())
                        list_down.append(url)
                #构建最后的str
                if list_down != []:
                    str_down = '#'.join(list_down)
                    send_mysql(name, str_down, ftype)

def send_mysql(name, str_down, ftype):
    '''将数据写入数据库'''
    sql = "insert into piaohua(name, content, type) value ('%s', '%s', '%s')"%(name,str_down,ftype)
    connect = mysql_connect.MysqlConnect('./misc/mysql_data.yaml')
    code = connect.change_data('spiderdata', sql)
    if code == 0:
        print('%s ok'%name)
    else:
        print('%s error,message: %s'%(name, code))


if __name__ == '__main__':
    ftype = input("需要下载的类型:\n<dongzuo,xiju,aiqing,kehuan,juqing,xuannian,wenyi,zhanzheng,kongbu,zainan,lianxuju,dongman>\n:")
    f = get_url(ftype)
    get_download_url(f,ftype)
