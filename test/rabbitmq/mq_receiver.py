# pylint: disable=no-member
# -*- encoding: utf-8 -*-
'''
@File    :   mq_receiver.py
@Time    :   2020/07/06 18:13:49
@Author  :   Kellan Fan 
@Version :   1.0
@Contact :   kellanfan1989@gmail.com
@Desc    :   None
'''

# here put the import lib
from mq_sender import SenderClient

class ReceiverClient(SenderClient):
    """
    接收rabbitmq消息的消费者
    """
    def run(self,queuename=None):
        """
        从mq中接收消息。
        :return:
        """
        if not hasattr(self, 'channel') or self.channel.is_closed:
            self.channel_mq()

        if not queuename:
            queuename = self.queue
        self.channel.basic_qos(prefetch_count=1)
        # 订阅消息
        self.channel.basic_consume(queue=queuename,
                                    on_message_callback=self.callback)
        # 循环等待
        self.channel.start_consuming()

    def diy(self, body):
        """
            需要重写该方法
        """
        print(body)


    def callback(self,ch, method, properties, body):
        """
         # 接收消息处理函数
        :param ch:
        :param method:
        :param properties:
        :param body:
        :return:
        """
        print('接收成功！')
        self.diy(body)
        # 发送确认
        ch.basic_ack(delivery_tag=method.delivery_tag)