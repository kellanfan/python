#coding=utf8
"""
# Author: Kellan Fan
# Created Time : Mon 06 Jul 2020 09:26:02 AM CST

# File Name: 01-simplereceive.py
# Description:

"""
import random
import pika
import time
#连接MQ
credentials = pika.PlainCredentials('admin','Zhu88jie')
conn = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq',credentials=credentials))
channel = conn.channel()
#声明交换机,类型为fanout
channel.exchange_declare(exchange='logs', exchange_type='fanout')
#声明队列
result = channel.queue_declare(queue='', auto_delete=True)
#将交换机和队列绑定
queue_name = result.method.queue
channel.queue_bind(exchange='logs',
                   queue=queue_name)

def callback(ch, method, properties, body):
    print(" [x] Receive {}".format(body))
    time.sleep(random.randint(1,5))
    print(" [x] Done")

channel.basic_consume(queue=queue_name,
                      on_message_callback=callback)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
