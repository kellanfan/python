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
from misc import pg_client
from misc import openurl
from log.create_logger import create_logger
logger = create_logger()

def get_downlink(url_part):
    str_down = ''
    url = 'http://www.meijutt.tv' + url_part
    ourl = openurl.OpenUrl(url,'gb2312')
    code,doc = ourl.run()
    if code == 200:
        selecter = etree.HTML(doc)
        try:
            name = selecter.xpath("//div[@class='info-title']/h1/text()")[0]
            links = selecter.xpath("//input[@name='down_url_list_0']/following-sibling::p/strong/a/@href")
            status = selecter.xpath('//div[@class="o_r_contact"]/ul/li[1]/font[1]/text()')[0]
        except Exception as e:
            print(e)
            return 'null','null','null'
        else:
            str_down = '#'.join(links)
        return name, str_down, status
    else:
        return 'null','null','null'

def send_pg(pg_conn, para):
    sql = "insert into meiju(name, content, status) values (%s, %s, %s)"
    code = pg_conn.execute(sql,para)
    if code:
        logger.info('insert [{}] ok'.format(para[0]))
    else:
        logger.error('insert [{0}] error, message: [{1}]'.format(para,code))

def get_status(pg_conn,name):
    sql = "select status from meiju where name = '{}'".format(name)
    return pg_conn.execute(sql)

def update_pg(pg_conn,para):
    sql = "update meiju set content ='{}',status = '{}' where name = '{}'".format(para[1],para[2],para[0])
    ret = pg_conn.execute(sql)
    if ret == 0:
        logger.error('update sql failed..')
    else:
        logger.info('update [{}] ok..'.format(para[0]))

def page_link(url):
    '''获取页面的每个美剧的url信息'''
    ourl = openurl.OpenUrl(url,'gb2312')
    code,doc = ourl.run()
    if code == 200:
        selecter = etree.HTML(doc)
        return selecter.xpath("//a[@class='B font_14']/@href")
    else:
        return [] 

def main():
    print("欢迎使用 美剧天堂 爬取脚本")
    pg_conn = pg_client.Mypostgres()
    for ftype in range(1,7):
        start_url="http://www.meijutt.tv/file/list{}.html".format(ftype)
        ourl = openurl.OpenUrl(start_url, 'gb2312')
        code,doc = ourl.run()    
        if code == 200:
            selecter = etree.HTML(doc)
            pages = selecter.xpath("//div[@class='page']/span/text()")[0].split()[0].split('/')[1]
            firstpage_links = selecter.xpath("//a[@class='B font_14']/@href")
            for firstpage_link in firstpage_links:
                name, download_links, status = get_downlink(firstpage_link)
                print(name,status)
                if name != 'null':
                    ret_status = get_status(pg_conn, name)
                    if not ret_status:
                        send_pg(pg_conn,[name, download_links, status])
                    elif status != ret_status:
                        update_pg(pg_conn,[name, download_links, status])
                    else:
                        pass

                time.sleep(0.5)

            for page in range(2,int(pages)):
                page_url = 'http://www.meijutt.tv/file/list{0}_{1}.html'.format(ftype,page)
                for link in page_link(page_url):
                    name,download_links,status = get_downlink(link)
                    print(name)
                    if name != 'null':
                        ret_status = get_status(pg_conn, name)
                        if not ret_status:
                            send_pg(pg_conn,[name, download_links, status])
                        elif status != ret_status:
                            update_pg(pg_conn,[name, download_links, status])
                        else:
                            pass
                    time.sleep(0.5)
        else:
            print("[{}] error...".format(start_url))

    print("Done.")
if __name__ == '__main__':
    main()