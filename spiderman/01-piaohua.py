#coding=utf8
"""
# Author: kellanfan
# Created Time : Sun 07 Apr 2019 01:52:30 PM CST

# File Name: 01-piaohua.py
# Description:

"""
import os
import re
import time
import operator
import redis
import argparse
from lxml import etree
from misc.openurl import OpenUrl
from misc.pg_client import Mypostgres

class PiaohuaSpider(object):
    '''
        通过url获取需要的数据
    '''
    def __init__(self, url):
        self.html = self.gethtml(url)
        if self.html:
            self.selector = etree.HTML(self.html)
            self.pages = self.get_pages()
            self.updatetime = self.get_updatetime()
            self.moivename = self.get_name()
            self.page_url = self.get_one_page_url()
            self.down_url = self.get_down_url()
            self.public_time = self.get_moive_public()

    def gethtml(self, url):
        '''
           获取html文件
           返回url的列表
        '''
        ob_openurl = OpenUrl(url)
        code, html = ob_openurl.run()
        if code == 200:
            return html
        else:
            print('open [{}] failed..'.format(url))

    def get_pages(self):
        '''
           获取到该类型的总页数
           返回 数字类型的总页数
        '''
        p = re.compile(r'共(\d+)页')
        temp = p.search(self.html)
        if temp:
            return int(temp.group(1))

    def get_updatetime(self):
        '''
           获取本页中最后一项的更新时间
           返回月日的字符串
        '''
        p = re.compile(r'(\d+-\d+)')
        temp = self.selector.xpath("//div[@class='txt']/span/text()")
        if temp:
            string = p.search(temp[-1].strip())
            if string:
                return string.group()

    def get_one_page_url(self):
        '''
           获取本页中电影主页的url列表
           返回url列表
        '''
        temp = self.selector.xpath("//div[@class='txt']/h3/a/@href")
        if temp:
            return temp

    def get_name(self):
        '''
           获取电影名称
           返回电影名称的字符串
        '''
        name = self.selector.xpath("//div[@class='info']/span[1]/text()")
        if name:
            return name[0].split('：')[-1]

    def get_moive_public(self):
        '''
            获取电影发布时间
        '''
        public = self.selector.xpath("//div[@class='info']/span[2]/text()")
        if public:
            return public[0].split('：')[-1]

    def get_down_url(self):
        '''
           获取下载地址，只获取magnet和ftp类型的地址
           返回一个字符串，如果是多个url地址，那么使用#做分割
        '''
        l = []
        seg = '###'
        for item in self.selector.xpath("//a/text()"):
            item = item.strip()
            if item.startswith('magnet') or item.startswith('ftp'):
                l.append(item)
        lenth = len(l)
        if lenth == 0:
            return None
        elif lenth == 1:
            return l[0]
        else:
            return seg.join(l)

def send_pg(name, ftype, public_time, down_url, connect):
    '''将数据写入数据库'''
    sql = "insert into piaohua(name, content, type, updatetime) values ('%s', '%s', '%s', '%s')"%(name,down_url,ftype,public_time)
    code = connect.change_data(sql)
    if code == 0:
        print('[{}] ok'.format(name))
    else:
        print('[{}] error,message: [{}]'.format(name, code))


def main(args):
    '''
        主函数，调度器
    '''
    redis_pool = redis.ConnectionPool(host='192.168.1.2',port=6379)
    redis_conn = redis.Redis(connection_pool=redis_pool)
    pg_conn = Mypostgres()

    ftype_list = ['xiju', 'dongzuo', 'aiqing', 'kehuan', 
                  'juqing', 'xuannian', 'zhanzheng', 'kongbu',
                  'zainan', 'dongman']
    #将获取到的电影url存入到redis中
    for ftype in ftype_list:
        url = 'https://www.piaohua.com/html/{}/'.format(ftype)
        pri = 1
        pages = PiaohuaSpider(url).pages
        for page in range(1,int(pages)):
            page_list_url = url + 'list_' + str(page) + '.html'
            piaohua = PiaohuaSpider(page_list_url)
            if not piaohua.html:
                continue
            for page_u in piaohua.page_url:
                redis_conn.zadd(ftype, {page_u: pri})
                pri += 1
            time.sleep(0.5)
    time.sleep(5)
    #从redis中获取url，获取数据，并写入数据库
    if args.update:
        current_updatetime = pg_conn.select_data('select updatetime from piaohua order by updatetime desc limit by 1')
    elif args.all:
        current_updatetime = '2000-01-01'
    for fkey in ftype_list:
        for value in redis_conn.zrange(fkey,0,-1):
            moive = PiaohuaSpider('https://www.piaohua.com' + value.decode('utf-8'))
            print('get [{}]'.format(moive.moivename))
            if not moive.html or not moive.down_url:
                print('get [{}] failed'.format(moive.moivename))
                continue
            public_time = moive.public_time
            if operator.gt(current_updatetime, public_time):
                break
            send_pg(moive.moivename, fkey, moive.public_time, moive.down_url, pg_conn)
            time.sleep(0.5)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--all', help='获取全部数据', action="store_true")
    parser.add_argument('-u', '--update', help='更新数据', action="store_true")
    args= parser.parse_args()
    if not args.all and not args.update:
        print("请使用-h获取帮助信息..")
        exit()
    main(args)
