#coding=utf8
"""
# Author: Kellan Fan
# Created Time : Mon 06 Jul 2020 03:28:28 PM CST

# File Name: 06-rpc-client.py
# Description:

"""
import pika
import uuid
import sys

class FibonacciRpcClient(object):
    def __init__(self):
        credentials = pika.PlainCredentials('admin','Zhu88jie')
        self.conn = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq',credentials=credentials))
        self.channel = self.conn.channel()
        result = self.channel.queue_declare(queue='', auto_delete=True)
        self.callback_queue = result.method.queue
        self.channel.basic_consume(queue=self.callback_queue, on_message_callback=self.on_response)
	
    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, n):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(exchange='',
                                   routing_key='rpc_queue',
                                   properties=pika.BasicProperties(
                                         reply_to = self.callback_queue,
                                         correlation_id = self.corr_id,
                                         ),
                                   body=str(n))
        while self.response is None:
            self.conn.process_data_events()
        return int(self.response)

fibonacci_rpc = FibonacciRpcClient()
num = sys.argv[1] if len(sys.argv) == 2 else 30
print(" [x] Requesting fib({})".format(num))
response = fibonacci_rpc.call(num)
print(" [.] Got {}".format(response))
