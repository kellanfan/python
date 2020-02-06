# pylint: disable=no-member
# -*- encoding: utf-8 -*-
'''
@File    :   qiushibaike.py
@Time    :   2020/02/05 15:58:41
@Author  :   Kellan Fan 
@Version :   1.0
@Contact :   kellanfan1989@gmail.com
@Desc    :   None
'''

# here put the import lib

import os
from lxml import etree
from misc import openurl
from misc import pg_client

def send_pg(connect,item):
        '''将数据写入数据库'''
        sql = "insert into qiubai(imgurl, username, content, vote, comment) value ('%s', '%s', '%s', '%s', '%s')"%(item['imgUrl'], item['username'], item['content'], item['vote'], item['comment'])
        ret = connect.execute(sql)
        if ret:
            print('[{}] ok'.format(item['username']))
        else:
            print('[{0}] error,message: [{1}]'.format(item['username'], ret))

def spiderman():
    url = 'https://www.qiushibaike.com/8hr/page/1/'
    ourl = openurl.OpenUrl(url)
    code, doc = ourl.run()
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
    items = spiderman()
    pg_conn = pg_client.Mypostgres()
    for item in items:
        send_pg(pg_conn, item)

if __name__ == '__main__':
    main()
