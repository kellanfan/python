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
            if not name or not links:
                name = 'null'
                str_down = 'null'
        except:
            name = 'null'
            str_down = 'null'
        else:
            str_down = '#'.join(links)

        return name, str_down
    else:
        return 'null','null'

def send_pg(name, str_down):
    sql = "insert into meiju(name, content) values ('%s', '%s')"%(name,str_down)
    connect = pg_client.Mypostgres()
    code = connect.change_data(sql)
    if code == 0:
        print('[{}] ok'.format(name))
    else:
        print('{} error, message: {}'.format(name,code))

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
    print("="*20)
    print("魔幻/科幻：1\n灵异/惊悚：2\n都市/感情：3\n犯罪/历史：4\n选秀/综艺：5\n动漫/卡通：6")
    print("="*20)
    ftype = input('请输入需要爬取的类型的代号：')
    start_url="http://www.meijutt.tv/file/list%s.html" %ftype
    ourl = openurl.OpenUrl(start_url,'gb2312')
    code,doc = ourl.run()
    if code == 200:
        selecter = etree.HTML(doc)
        pages = selecter.xpath("//div[@class='page']/span/text()")[0].split()[0].split('/')[1]
        firstpage_links = selecter.xpath("//a[@class='B font_14']/@href")
        for firstpage_link in firstpage_links:
            name,download_links = get_downlink(firstpage_link)
            send_pg(name, download_links)
            time.sleep(0.5)

        for page in range(2,int(pages)):
            page_url = 'http://www.meijutt.tv/file/list%s_%s.html'%(ftype,page)
            for link in page_link(page_url):
                name,download_links = get_downlink(link)
                if name != '' and download_links != '':
                    send_pg(name, download_links)
                    time.sleep(0.5)
    else:
        print("[%s] error..."%start_url)
    
    print("Done.")
if __name__ == '__main__':
    main()