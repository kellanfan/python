#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Sat 05 May 2018 09:57:24 AM CST

# File Name: piaohua.py
# Description: 爬取飘花网的电影资源

"""
import os
import re
import time
import sys
import redis
#发现re确实不好处理一些特殊的html，改动bs4
from bs4 import BeautifulSoup
from lxml import etree
from misc import mysql_connect
from misc import openurl
from misc.logger import Logger

class Piaohua(object):
    def __init__(self,ftype):
        self.__ftype = ftype
        self.__redis_link = self.__redis_connect()
        mylog = Logger(os.path.join(os.path.abspath(os.path.curdir),'misc/spider_log.yaml'))
        self.__logger = mylog.outputLog()

    def __redis_connect(self):
        pool = redis.ConnectionPool(host='127.0.0.1',port=6379)
        return redis.Redis(connection_pool=pool)

    def get_url(self):
        main_url = 'https://www.piaohua.com/html/%s/index.html' %self.__ftype
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
        redis_id = 0
        for page in range(1,int(pages)):
            list_url = 'https://www.piaohua.com/html/%s/list_%d.html' %(self.__ftype, page)
            sub_ourl = openurl.OpenUrl(list_url)
            sub_code,sub_content = sub_ourl.openurl()
            if sub_code == 200:
                selector = etree.HTML(sub_content)
                for link in selector.xpath('//span/a'):
                    sub_url = link.attrib['href']
                    if sub_url.startswith('/html/'+ self.__ftype ):
                        fkey = self.__ftype + str(redis_id)
                        self.__redis_link.set(fkey, sub_url, ex=21600)
                        redis_id += 1
            time.sleep(0.5)

    def get_download_url(self):
        '''主要函数'''
        redis_id = 0
        while True:
            fkey = self.__ftype + str(redis_id)
            line = self.__redis_link.get(fkey)
            redis_id += 1
            if line:
                 #构建url
                 url = 'https://www.piaohua.com' + line.decode()
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
                         if not url is None and 'ftp' in url:
                            url = ''.join(url.split())
                            list_down.append(url)
                         else:
                            continue
                     #构建最后的str
                     if list_down != []:
                         str_down = '#'.join(list_down)
                         self.send_mysql(name, str_down)
                     else:
                         self.__logger.error("[ %s ] can not find dowload link..." %name)
                 else:
                     self.__logger.critical("bad url: [ %s ]" %url)
            else:
                break


    def send_mysql(self, name, str_down):
        '''将数据写入数据库'''
        sql = "insert into piaohua(name, content, type) value ('%s', '%s', '%s')"%(name,str_down,self.__ftype)
        connect = mysql_connect.MysqlConnect(os.path.join(os.path.abspath(os.path.curdir),'misc/mysql_data.yaml'))
        code = connect.change_data('spiderdata', sql)
        if code == 0:
            self.__logger.info('[%s] ok'%name)
        else:
            self.__logger.error('[%s] error,message: [%s]'%(name, code))


if __name__ == '__main__':
    ftype = input("需要下载的类型:\n<dongzuo,xiju,aiqing,kehuan,juqing,xuannian,wenyi,zhanzheng,kongbu,zainan,lianxuju,dongman>\n:")
    piaohua = Piaohua(ftype)
    piaohua.get_url()
    piaohua.get_download_url()
