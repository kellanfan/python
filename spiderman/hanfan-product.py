# pylint: disable=no-member
# -*- encoding: utf-8 -*-
'''
@File    :   hanfan-product.py
@Time    :   2019/12/20 00:10:55
@Author  :   Kellan Fan 
@Version :   1.0
@Contact :   kellanfan1989@gmail.com
@Desc    :   None
'''

# here put the import lib
import sys
import time
import pika
from lxml import etree
from misc.openurl import OpenUrl


def get_url(ftype,channel):
    main_url = 'https://www.hanfan.cc/'
    ourl = OpenUrl(main_url + ftype)
    code,main_content = ourl.run()
    if code == 200:
        selecter = etree.HTML(main_content)
        pages = int(selecter.xpath('/html/body/section/div[1]/div/div[2]/ul/li[8]/span/text()')[0].split(' ')[1])
    else:
        print("bad url: {}".format(main_url))
        sys.exit()
    for page in range(1,pages):
        page_url = main_url + ftype + '/page/%s/'%page
        sub_ourl = OpenUrl(page_url)
        sub_code,sub_content = sub_ourl.run()
        if sub_code == 200:
            selecter = etree.HTML(sub_content)
            selecter_list = selecter.xpath('//article/header/h2/a')
            for link in selecter_list:
                name = link.text
                sub_url = link.attrib['href'] + '#prettyPhoto/0/'

                channel.basic_publish(exchange='',
                    routing_key='hanfan',
                    body=str({name:sub_url}),
                    properties=pika.BasicProperties(
                    delivery_mode=2,
                    ))
        else:
            continue
        time.sleep(1)

connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.1.252'))
channel = connection.channel()
channel.queue_declare(queue='hanfan', durable=True)  