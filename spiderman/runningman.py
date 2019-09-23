#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re
import os,sys
import time
from lxml import etree
from misc import openurl
from misc import mysql_connect
from misc.logger import Logger


def get_links(year):
    start_url = 'http://www.runningman-fan.com/category/runningman%s' %year
    allurl_list = []
    for page in range(1,20): #这块需要根据具体页数进行循环
        full_url = start_url + '/page/%d' %page
        ourl = openurl.OpenUrl(full_url)
        code, doc = ourl.openurl()
        time.sleep(0.5)
        if code == 200:
            selecter = etree.HTML(doc)
            url_list = selecter.xpath('//h2[@class="entry-title"]/a/@href')
            title_list = selecter.xpath('//h2[@class="entry-title"]/a/text()')
            if not title_list:
                continue
            me = dict(zip(title_list, url_list))
            for title in title_list:
                if u'高清中字' in title:
                    allurl_list.append(me[title])
    return allurl_list

def downurl(allurl, logger):
    for url in allurl:
        info = []
        phase = re.sub('\D', "", url)
        ourl = openurl.OpenUrl(url)
        code, doc = ourl.openurl()
        if code == 200:
            selecter = etree.HTML(doc)
            try:
                down_link = selecter.xpath('//div[@class="buttons"]/a/@href')[0]
                passwd = selecter.xpath('//div[@class="buttons"]/a/text()')[0]
            except:
                logger.error('%s get info error...'%phase)
                continue
        info.append(phase)
        info.append(down_link)
        info.append(passwd)
        send_mysql(info, logger)


def send_mysql(info, logger):
    sql = "insert into runningman(phase, panurl, password) value ('%s', '%s', '%s')"%(info[0],info[1],info[2])
    connect = mysql_connect.MysqlConnect('./misc/mysql_data.yaml')
    code = connect.change_data(sql)
    if code == 0:
        logger.info('%s ok'%info[0])
    else:
        logger.error('%s error,message: %s'%(info[0],code))

def main():
    mylog = Logger(os.path.join(os.path.abspath(os.path.curdir),'misc/spider_log.yaml'))
    logger = mylog.outputLog()
    year = input("请输入年份：")
    allurl = get_links(year)
    downurl(allurl, logger)

if __name__ == '__main__':
    main()
