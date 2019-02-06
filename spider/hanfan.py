#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Tue 29 Jan 2019 06:53:36 PM CST

# File Name: hanfan.py
# Description:

"""
import os, sys, time
import redis
from lxml import etree
from misc.openurl import OpenUrl
from misc import mysql_connect
from misc.logger import Logger

class Hanfan(object):
    def __init__(self):
        self.__redis_link = self.__redis_connect()
        mylog = Logger(os.path.join(os.path.abspath(os.path.curdir),'misc/spider_log.yaml'))
        self.__logger = mylog.outputLog()
        self.mysql_connect = mysql_connect.MysqlConnect(os.path.join(os.path.abspath(os.path.curdir),'misc/mysql_data.yaml'))

    def __redis_connect(self):
        pool = redis.ConnectionPool(host='127.0.0.1',port=6379)
        return redis.Redis(connection_pool=pool)
    
    def get_url(self):
        main_url = 'http://www.hanfan.cc/movie/'
        ourl = OpenUrl(main_url)
        code,main_content = ourl.openurl()
        if code == 200:
            selecter = etree.HTML(main_content)
            pages = int(selecter.xpath('/html/body/section/div/div/div[3]/ul/li[8]/span/text()')[0].split(' ')[1])
        else:
            print("bad url: %s" %main_url)
            sys.exit()

        for page in range(1,pages):
            page_url = 'http://www.hanfan.cc/movie/page/%s/'%page
            sub_ourl = OpenUrl(page_url)
            sub_code,sub_content = sub_ourl.openurl()
            if sub_code == 200:
                selecter = etree.HTML(sub_content)
                selecter_list = selecter.xpath('//article/header/h2/a')
                for link in selecter_list:
                    name = link.text
                    sub_url = link.attrib['href'] + '#prettyPhoto/0/'
                    self.__redis_link.set(name, sub_url, ex=21600)
            time.sleep(1)
                    
    def get_download_url(self):
        redis_keys = self.__redis_link.keys()
        for fkey in redis_keys:
            url = self.__redis_link.get(fkey)
            ourl = OpenUrl(url)
            code,content = ourl.openurl()
            if code == 200:
                selecter = etree.HTML(content)
                try:
                    cloudpan_url = selecter.xpath('//div[@class="part"]/a/@href')
                    if len(cloudpan_url) == 1:
                        cloudpan_url = cloudpan_url[0]
                        cloudpan_pass = selecter.xpath('//div[@class="part"]/text()')[2]
                    elif len(cloudpan_url) == 2:
                        cloudpan_url = '|'.join(cloudpan_url)
                        cloudpan_pass = '|'.join(selecter.xpath('//div[@class="part"]/text()')[2:4])
                    else:
                        self.__logger.error('[%s] donot has cloudpan download link...'%fkey)
                        continue
                except:
                    self.__logger.error('[%s] miss something..'%fkey)
                    continue
                self.send_mysql(fkey, cloudpan_url, cloudpan_pass)
            else:
                self.__logger.error('[%s] can not open the download page..'%fkey)
                continue
            time.sleep(0.5)

    def send_mysql(self, name, cloudpan_url, cloudpan_pass):
        '''将数据写入数据库'''
        sql = "insert into hanfan(name, url, panpass) value ('%s', '%s', '%s')" %(name.decode(),cloudpan_url,cloudpan_pass)
        print(sql)
        code = self.mysql_connect.change_data('spiderdata', sql)
        if code == 0:
            self.__logger.info('[%s] ok'%name)
        else:
            self.__logger.error('[%s] error,message: [%s]'%(name, code))

if __name__ == '__main__':
    a = Hanfan()
    #a.get_url()
    a.get_download_url()
