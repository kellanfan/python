#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Sun 25 Nov 2018 07:50:36 PM CST

# File Name: qiushibaike.py
# Description:

"""
import os
from lxml import etree
from misc import openurl
from misc import mysql_connect
from misc.logger import Logger


def send_mysql(item, logger):
        '''将数据写入数据库'''
        sql = "insert into qiubai(imgurl, username, content, vote, comment) value ('%s', '%s', '%s', '%s', '%s')"%(item['imgUrl'], item['username'], item['content'], item['vote'], item['comment'])
        connect = mysql_connect.MysqlConnect(os.path.join(os.path.abspath(os.path.curdir),'misc/mysql_data.yaml'))
        code = connect.change_data('spiderdata', sql)
        if code == 0:
            logger.info('[%s] ok'%item['username'])
        else:
            logger.error('[%s] error,message: [%s]'%(item['username'], code))

def spiderman():
    url = 'https://www.qiushibaike.com/8hr/page/1/'
    ourl = openurl.OpenUrl(url)
    code, doc = ourl.openurl()
    if code == 200:
        selector = etree.HTML(doc)
        content = selector.xpath("//div[contains(@id,'qiushi_tag')]")
        item = []
        for site in content:
            result = {}
            try:
                imgUrl = site.xpath('./div/a/img/@src')[0]
                username = site.xpath('./div/a/img/@alt')[0]
                content = site.xpath('.//div[@class="content"]/span/text()')[0].strip()
                vote = site.xpath('.//i/text()')[0]
                comment = site.xpath('.//i/text()')[1]
            except:
                print("something failed..")
                continue

            result['imgUrl'] = imgUrl
            result['username'] = username
            result['content'] = content
            result['vote'] = vote
            result['comment'] = comment
            
            item.append(result)
    
    return item

def main():
    mylog = Logger(os.path.join(os.path.abspath(os.path.curdir),'misc/spider_log.yaml'))
    logger = mylog.outputLog()
    items = spiderman()
    for item in items:
        send_mysql(item, logger)

if __name__ == '__main__':
    main()
