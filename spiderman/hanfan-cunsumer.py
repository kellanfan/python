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

def send_pg(fkey, cloudpan_url, cloudpan_pass):
    sql = "insert into hanfan(name,url,panpass) values ('{}', '{}', '{}')".format(fkey, cloudpan_url, cloudpan_pass)
    ret = pg_connect.change_data(sql)
    if ret == 0:
        print('insert [{}] ok...'.format(fkey))
    else:
        print(ret)
        sys.exit()

def callback(ch, method, properties, body):  # 四个参数为标准格式
    # 管道内存对象  内容相关信息  后面讲
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
        send_pg(fkey, cloudpan_url, cloudpan_pass)
    else:
        pass
    time.sleep(0.5)
    ch.basic_ack(delivery_tag = method.delivery_tag)  # 告诉生成者，消息处理完成
pg_connect = pg_client.Mypostgres()
connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.1.252'))
channel = connection.channel()
channel.queue_declare(queue='hanfan', durable=True, arguments={'x-max-length':20000})
channel.basic_consume(  # 消费消息
        'hanfan',  # 你要从那个队列里收消息
        callback,  # 如果收到消息，就调用callback函数来处理消息
        # no_ack=True  # 写的话，如果接收消息，机器宕机消息就丢了
        # 一般不写。宕机则生产者检测到发给其他消费者
        )

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()