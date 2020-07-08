# pylint: disable=no-member
# -*- encoding: utf-8 -*-
'''
@File    :   mq_sender.py
@Time    :   2020/07/06 17:26:11
@Author  :   Kellan Fan 
@Version :   1.0
@Contact :   kellanfan1989@gmail.com
@Desc    :   None
'''

# here put the import lib
import pika

class SenderClient(object):
    def __init__(self, username, passwd, host="rabbitmq", port=5672,
                 queuename='kellan', exchange='kellan', 
                 exchange_type='direct', routing_key='kellan'):
        self.__host = host
        self.__port = port
        self.__username = username
        self.__passwd = passwd
        self.queue = queuename
        self.__exchange = exchange
        self.__exchange_type = exchange_type
        self.__routing_key = routing_key

    def connect_mq(self):
        """
        连接mq
        :return:
        """
        try:
            # 创建一个连接对象
            if not hasattr(self, 'connection') or self.connection.is_closed:
                # 添加用户名和密码
                credentials = pika.PlainCredentials(self.__username, self.__passwd)
                # 配置连接参数
                parameters = pika.ConnectionParameters(host=self.__host, port=self.__port, credentials=credentials)
                self.connection = pika.BlockingConnection(parameters)
        except Exception as e:
            print(e)

    def channel_mq(self):
        """
        # 创建一个信道
        # 声明队列和交换机和绑定
        :return:
        """
        if not hasattr(self, "connection"):
            self.connect_mq()
        if not hasattr(self, 'channel') or self.channel.is_closed:
            self.channel = self.connection.channel()

        # 声明一个队列,durable参数声明队列持久化
        self.channel.queue_declare(queue=self.queue, durable=True)
        self.channel.exchange_declare(exchange=self.__exchange, exchange_type=self.__exchange_type, durable=True)
        # 交换机和队列绑定:生产者发布消息时无需绑定，消费者消费消息时需要绑定
        self.channel.queue_bind(exchange=self.__exchange, queue=self.queue, routing_key=self.__routing_key)

    def send_data(self, data):
        """
        # 发送数据
        :param channel:
        :return:
        """
        self.channel_mq()
        # 使用默认交换机投递消息,返回TRUE或False
        self.channel.basic_publish(exchange=self.__exchange,
                                  routing_key=self.__routing_key,
                                  body=data,
                                  properties=pika.BasicProperties(delivery_mode=2))

    def close_connect(self):
        """
        # 关闭tcp连接
        :return:
        """
        self.connection.close()

    def close_channel(self, channel):
        """
        # 关闭信道
        :param channel:
        :return:
        """
        if not hasattr(self, 'channel'):
            raise ValueError("the object of SenderClient has not attr of channel.")
        self.channel.close()