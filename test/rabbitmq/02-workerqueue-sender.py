#coding=utf8
"""
# Author: Kellan Fan
# Created Time : Mon 06 Jul 2020 09:23:48 AM CST

# File Name: 01-simplesender.py
# Description:

"""
import pika
import sys

credentials = pika.PlainCredentials('admin','Zhu88jie')
conn = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq',credentials=credentials))

channel = conn.channel()
channel.queue_declare(queue='hello', durable=True) #durable=True 持久化队列
message = ' '.join(sys.argv[1:]) or 'Hello World!'
channel.basic_publish(exchange='', 
                      routing_key='hello', 
                      body=message,
                      properties=pika.BasicProperties(
                          delivery_mode = 2,  #持久化消息
                      ))
print(" [x] Sent {}".format(message))

conn.close()
