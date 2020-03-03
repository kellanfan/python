# pylint: disable=no-member
# -*- encoding: utf-8 -*-
'''
@File    :   gushiwen.py
@Time    :   2020/03/02 15:05:03
@Author  :   Kellan Fan 
@Version :   1.0
@Contact :   kellanfan1989@gmail.com
@Desc    :   爬取古诗文
'''

# here put the import lib
import time
from lxml import etree
from log.create_logger import create_logger
from misc.openurl import OpenUrl
from misc.pg_client import Mypostgres

logger = create_logger()

def get_guwen_list(html):
    selecter = etree.HTML(html)
    links= []
    for sub_selector in selecter.xpath('//div[@class="typecont"]'):
        links += sub_selector.xpath('//a/@href')
    return links    

def send_pg(pg_conn, para):
    sql = 'insert into gushici(name, dynasty, author, content) values (%s, %s, %s, %s)'
    code = pg_conn.execute(sql,para)
    if code == 1:
        logger.info('[{}] ok'.format(para))
    else:
        logger.error('[{0}] error, message: [{1}]'.format(para,code))

def main():
    start_url = 'https://so.gushiwen.org'
    guwen_list = ['tangshi', 'songci']
    pg_conn = Mypostgres()
    for guwen in guwen_list:
        url = start_url + '/gushi/' + guwen + '.aspx'
        ourl = OpenUrl(url)
        code, doc = ourl.run()
        if code != 200:
            logger.error('Get the [{0}] failed, the Code is [{1}]'.format(url,code))
            continue
        for link in get_guwen_list(doc):
            if not link.startswith('/shiwenv'):
                continue
            sub_url = start_url + link
            ourl = OpenUrl(sub_url)
            code, html = ourl.run()
            if code != 200:
                logger.error('Get the [{0}] failed, the Code is [{1}]'.format(sub_url,code))
                continue
            logger.info('handle the [{}]'.format(sub_url))
            sub_selector = etree.HTML(html)
            name = sub_selector.xpath('//h1/text()')[0]
            dynasty = sub_selector.xpath('//p[@class="source"]/a/text()')[0]
            author = sub_selector.xpath('//p[@class="source"]/a/text()')[1]
            content_list = sub_selector.xpath('//div[@class="contson"]/text()')
            for conts in content_list:
                if conts.endswith('\n'):
                    index=content_list.index(conts)
                    break
            content = ' '.join(content_list[0:index+1])
            send_pg(pg_conn,(name,dynasty, author, content.strip()))
            time.sleep(0.5)
if __name__ == "__main__":
    main()