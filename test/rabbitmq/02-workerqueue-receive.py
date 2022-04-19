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
credentials = pika.PlainCredentials('admin','Zhu88jie')
conn = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq',credentials=credentials))

channel = conn.channel()

channel.queue_declare(queue='hello', durable=True)

def callback(ch, method, properties, body):
    print(" [x] Receive {}".format(body))
    time.sleep(random.randint(1,5))
    print(" [x] Done")
    ch.basic_ack(delivery_tag = method.delivery_tag)
channel.basic_qos(prefetch_count=1) #类似于权重，这样是告诉RabbitMQ，再同一时刻，不要发送超过1条消息给一个工作者（worker），直到它已经处理了上一条消息并且作出了响应。这样，RabbitMQ就会把消息分发给下一个空闲的工作者（worker）。
channel.basic_consume(queue='hello',
                      on_message_callback=callback)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
