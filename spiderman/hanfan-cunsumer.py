# pylint: disable=no-member
# -*- encoding: utf-8 -*-
'''
@File    :   hanfan-cunsumer.py
@Time    :   2019/12/21 16:47:42
@Author  :   Kellan Fan 
@Version :   1.0
@Contact :   kellanfan1989@gmail.com
@Desc    :   None
'''

# here put the import lib
import pika
import time
import json
import sys
from misc.openurl import OpenUrl
from lxml import etree
from misc import pg_client
from misc.mq_receiver import ReceiverClient

def send_pg(pg_connect,para):
    sql = "insert into hanfan(name,url,panpass) values (%s,%s,%s)"
    ret = pg_connect.execute(sql, para)
    if ret:
        print('insert [{}] ok...'.format(para))
    else:
        print('insert [{0}] failed: [{1}]'.format(para, ret))

def diy(body,pg_connect):
    cloudpan_url = 'null'
    cloudpan_pass = 'null'
    msg = eval(body)
    print('{} {}'.format(msg.keys(),msg.values()))
    fkey = list(msg.keys())[0]
    ourl = OpenUrl(msg[fkey])
    code,content = ourl.run()
    if code == 200:
        selecter = etree.HTML(content)
        try:
            cloudpan_url = selecter.xpath('//div[@class="part"]/a/@href')
            if len(cloudpan_url) == 1:
                cloudpan_url = cloudpan_url[0]
                cloudpan_pass = selecter.xpath('//div[@class="part"]/text()')[2]
            elif len(cloudpan_url) == 2:
                cloudpan_url = '|'.join(cloudpan_url)
                cloudpan_pass = '|'.join(selecter.xpath('//div[@class="part"]/text()')[2:4])
            else:
                cloudpan_url = cloudpan_url[0]
                cloudpan_pass = cloudpan_pass[0]
        except:
            pass
        send_pg(pg_connect,[fkey, cloudpan_url, cloudpan_pass])
    else:
        pass
    time.sleep(0.5)

def main():
    pg_connect = pg_client.Mypostgres()
    receiver = ReceiverClient('admin','Zhu88jie')
    receiver.diy = diy
    receiver.run()