#coding=utf8
"""
# Author: Kellan Fan
# Created Time : Mon 10 Feb 2020 11:56:52 AM CST

# File Name: simi.py
# Description:

"""
import string
import random
import re
import time
import requests
import redis
from lxml import etree
from misc.openurl import OpenUrl
from log.create_logger import create_logger

logger = create_logger()

def gen_uuid():
    uuid = ''.join(random.sample(string.ascii_lowercase + string.digits, 10))
    return uuid

def get_pages(start_url):
    url = start_url + '.html'
    ourl = OpenUrl(url)
    code, html = ourl.run()
    if code == 200:
        selecter = etree.HTML(html)
        pages_url = selecter.xpath('//div[@class="page"]/a/@href')[-1]
        pages = int(re.split('[/|.|-]', pages_url)[3])
    else:
        logger.error('get [{0}] failed: [{1}]'.format(url, code))
        pages = None
    return pages

def get_useful_url(start_url,redis_conn):
    all_page = get_pages(start_url)
    for page in range(1,all_page):
        if page == 1:
            url = start_url + '.html'
        else:
            url = start_url + '-' + str(page) + '.html'
        ourl = OpenUrl(url)
        code, html = ourl.run()
        if code == 200:
            selecter = etree.HTML(html)
            for urls in selecter.xpath('//a/@href'):
                if urls.startswith('/html'):
                    print(urls)
                    redis_conn.lpush('simi',urls)
        else:
            logger.error('get [{0}] failed: [{1}]'.format(url, code))

def get_img(redis_conn):
    start_url = 'https://se.haodd92.com/'
    for url in redis_conn.sort('simi',alpha=True):
        ourl = OpenUrl(start_url + url.decode('utf-8'))
        code, html = ourl.run()
        if code == 200:
            selecter = etree.HTML(html)
            img_url_list = selecter.xpath('//div[@class="center margintop border clear main"]/img/@src')
            for img_url in img_url_list:
                time.sleep(0.5)
                img_name = gen_uuid()
                local = 'image/{}.jpg'.format(img_name)
                try:
                    r = requests.get(img_url, stream=True)
                    with open(local, 'wb') as f:
                        f.write(r.content)
                    logger.info('download [{0}] to [{1}] successfully'.format(img_url,img_name))
                except Exception as e:
                    logger.error('download [{0}] to [{1}] failed: [{2}]'.format(img_url,img_name,e))

def main():
    start_url = 'https://se.haodd92.com/listhtml/7'
    try:
        redis_pool = redis.ConnectionPool(host='192.168.1.2',port=6379)
        redis_conn = redis.Redis(connection_pool=redis_pool)
        logger.info('Connect to redis successfully')
    except Exception as e:
        redis_conn = None
        logger.error('Connect to redis failed: [{}]'.format(e))
    get_useful_url(start_url，redis_conn)
    get_img(redis_conn)

if __name__ == "__main__":
    main()