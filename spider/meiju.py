#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Sat 06 Oct 2018 08:09:16 PM CST

# File Name: meiju.py
# Description:

"""
import os
import time
from lxml import etree
from misc import mysql_connect
from misc import openurl
from misc.logger import Logger

def get_downlink(url_part):
    str_down = ''
    url = 'http://www.meijutt.com' + url_part
    ourl = openurl.OpenUrl(url,'gb2312')
    code,doc = ourl.openurl()
    if code == 200:
        selecter = etree.HTML(doc)
        try:
            name = selecter.xpath("//div[@class='info-title']/h1/text()")[0]
            links = selecter.xpath("//input[@name='down_url_list_0']/following-sibling::p/strong/a/@href")
            if not name or not links:
                name = ''
                str_down = ''
        except:
            name = ''
            str_down = ''
        else:
            str_down = '#'.join(links)

        return name, str_down
    else:
        return '',''

def send_mysql(name, str_down,logger):
    sql = "insert into meiju(name, content) value ('%s', '%s')"%(name,str_down)
    connect = mysql_connect.MysqlConnect('./misc/mysql_data.yaml')
    code = connect.change_data(sql)
    if code == 0:
        logger.info('[%s] ok'%name)
    else:
        logger.error('%s error, message: %s'%(name,code))

def page_link(url):
    '''获取页面的每个美剧的url信息'''
    ourl = openurl.OpenUrl(url,'gb2312')
    code,doc = ourl.openurl()
    if code == 200:
        selecter = etree.HTML(doc)
        return selecter.xpath("//a[@class='B font_14']/@href")
    else:
        return []
        
    

def main():
    print("欢迎使用 美剧天堂 爬取脚本")
    print("="*20)
    print("魔幻/科幻：1\n灵异/惊悚：2\n都市/感情：3\n犯罪/历史：4\n选秀/综艺：5\n动漫/卡通：6")
    print("="*20)
    ftype = input('请输入需要爬取的类型的代号：')
    start_url="http://www.meijutt.com/file/list%s.html" %ftype
    ourl = openurl.OpenUrl(start_url,'gb2312')
    code,doc = ourl.openurl()
    mylog = Logger(os.path.join(os.path.abspath(os.path.curdir),'misc/spider_log.yaml'))
    logger = mylog.outputLog()
    if code == 200:
        selecter = etree.HTML(doc)
        pages = selecter.xpath("//div[@class='page']/span/text()")[0].split()[0].split('/')[1]
        firstpage_links = selecter.xpath("//a[@class='B font_14']/@href")
        for firstpage_link in firstpage_links:
            name,download_links = get_downlink(firstpage_link)
            send_mysql(name, download_links, logger)
            time.sleep(0.5)

        for page in range(2,int(pages)):
            page_url = 'http://www.meijutt.com/file/list%s_%s.html'%(ftype,page)
            for link in page_link(page_url):
                name,download_links = get_downlink(link)
                if name != '' and download_links != '':
                    send_mysql(name, download_links, logger)
                    time.sleep(0.5)
    else:
        print("[%s] error..."%start_url)
    
    print("Done.")
if __name__ == '__main__':
    main()
