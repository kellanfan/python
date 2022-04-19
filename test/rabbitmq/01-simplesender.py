#coding=utf8
"""
# Author: Kellan Fan
# Created Time : Mon 06 Jul 2020 09:23:48 AM CST

# File Name: 01-simplesender.py
# Description:

"""
import pika

credentials = pika.PlainCredentials('admin','Zhu88jie')
conn = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq',credentials=credentials))

channel = conn.channel()
channel.queue_declare(queue='hello')

channel.basic_publish(exchange='', 
                      routing_key='hello', 
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")

conn.close()
