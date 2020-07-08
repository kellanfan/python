#coding=utf8
"""
# Author: Kellan Fan
# Created Time : Mon 06 Jul 2020 09:26:02 AM CST

# File Name: 01-simplereceive.py
# Description:

"""
import sys
import random
import pika
import time
#连接MQ
credentials = pika.PlainCredentials('admin','Zhu88jie')
conn = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq',credentials=credentials))
channel = conn.channel()
#声明交换机,类型为fanout
channel.exchange_declare(exchange='topic_logs', exchange_type='topic')
#声明队列
result = channel.queue_declare(queue='', auto_delete=True)
#将交换机和队列绑定
queue_name = result.method.queue
binding_keys = sys.argv[1:]
if not binding_keys:
    print("Usage: %s [binding_key]..." %(sys.argv[0]))
    sys.exit(1)
for binding_key in binding_keys:
    channel.queue_bind(exchange='topic_logs',
                       queue=queue_name,
                       routing_key=binding_key)

def callback(ch, method, properties, body):
    print(" [x] Receive {0}:{1}".format(method.routing_key,body))
    time.sleep(random.randint(1,5))
    print(" [x] Done")

channel.basic_consume(queue=queue_name,
                      on_message_callback=callback)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
