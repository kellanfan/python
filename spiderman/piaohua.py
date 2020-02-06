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
from log.logger import logger
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

def send_pg(para, connect):
    '''将数据写入数据库'''
    sql = "insert into piaohua(name, type, updatetime, content, uri) values (%s, %s, %s, %s, %s)"
    code = connect.execute(sql,para)
    if code:
        print('insert [{}] ok'.format(para))
        logger.info('insert [{}] ok'.format(para))
    else:
        print('insert [{}] error,message: [{}]'.format(para, code))
        logger.error('insert [{}] error,message: [{}]'.format(para, code))

def main(args):
    '''
        主函数，调度器
    '''
    try:
        redis_pool = redis.ConnectionPool(host='192.168.1.2',port=6379)
        redis_conn = redis.Redis(connection_pool=redis_pool)
        pg_conn = Mypostgres()
    except:
        print('Connect to redis or postgresql failed')
        logger.error('Connect to redis or postgresql failed')
        
    ftype_list = ['xiju', 'dongzuo', 'aiqing', 'kehuan', 
                  'juqing', 'xuannian', 'zhanzheng', 'kongbu',
                  'zainan', 'dongman']

    #将获取到的电影url存入到redis中
    for ftype in ftype_list:
        try:
            cur_redis_uri = redis_conn.sort(ftype,alpha=True,desc=True)[0]
            cur_redis_uri = cur_redis_uri.decode('utf-8')
        except Exception as e:
            logger.error('redis dones not has the type [{}] keys,will get all'.format(ftype))
            cur_redis_uri = '/html/{}/2000/0101/00000.html'.format(ftype)
        logger.info('the type [{0}], cur_redis_utl is [{1}]'.format(ftype, cur_redis_uri))
        url = 'https://www.piaohua.com/html/{}/'.format(ftype)
        pages = PiaohuaSpider(url).pages
        for page in range(1,int(pages)):
            page_list_url = url + 'list_' + str(page) + '.html'
            piaohua = PiaohuaSpider(page_list_url)
            if not piaohua.html:
                continue
            if operator.ge(cur_redis_uri, piaohua.page_url[0]):
                break
            for page_u in piaohua.page_url:
                try:
                    redis_conn.lpush(ftype, page_u)
                    print("Put [{0}] into redis list successfully".format(page_u))
                    logger.info("Put [{0}] into redis list successfully".format(page_u))
                except Exception as e:
                    print("Put [{0}] into redis list failed:[{1}]".format(page_u, e))
                    logger.error("Put [{0}] into redis list failed:[{1}]".format(page_u, e))
            time.sleep(0.5)
    time.sleep(5)
    
    #从redis中获取url，获取数据，并写入数据库
    for ftype in ftype_list:
        if args.update:
            current_uri = pg_conn.execute("select uri from piaohua where type = '{}' order by uri desc limit 1".format(ftype))[0][0]
        elif args.all:
            current_uri= '/html/{}/2000/0101/00000.html'.format(ftype)
        print('Handling the [{}] type...'.format(ftype))
        logger.info('Handling the [{}] type...'.format(ftype))
        for value in redis_conn.sort(ftype,alpha=True,desc=True):
            value = value.decode('utf-8')
            if operator.ge(current_uri, value):
                print('the uri [{}] is timeout!'.format(value))
                logger.info('the uri [{}] is timeout!'.format(value))
                break
            moive = PiaohuaSpider('https://www.piaohua.com' + value) 
            if not moive.html or not moive.down_url:
                print('get [{}] failed'.format(moive.moivename))
                logger.error('get [{}] failed'.format(moive.moivename))
                continue
            else:
                print('get [{}] successfully'.format(moive.moivename))
                logger.info('get [{}] successfully'.format(moive.moivename))
            
            send_pg([moive.moivename, ftype, moive.public_time, moive.down_url, value], pg_conn)
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