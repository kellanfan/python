#coding=utf8
"""
# Author: Kellan Fan
# Created Time : Mon 06 Jul 2020 09:26:02 AM CST

# File Name: 01-simplereceive.py
# Description:

"""
import pika
credentials = pika.PlainCredentials('admin','Zhu88jie')
conn = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq',credentials=credentials))

channel = conn.channel()

channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    print(" [x] Receive {}".format(body))

channel.basic_consume(queue='hello',
                      on_message_callback=callback,
                      auto_ack=True)
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
