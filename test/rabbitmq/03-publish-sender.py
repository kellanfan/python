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
channel.exchange_declare(exchange='logs', exchange_type='fanout')
message = ' '.join(sys.argv[1:]) or 'Hello World!'
channel.basic_publish(exchange='logs', 
                      routing_key='', 
                      body=message,
                      )
print(" [x] Sent {}".format(message))

conn.close()
