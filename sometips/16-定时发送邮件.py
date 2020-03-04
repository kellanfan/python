# pylint: disable=no-member
# -*- encoding: utf-8 -*-
'''
@File    :   16-定时发送邮件.py
@Time    :   2020/03/03 08:12:55
@Author  :   Kellan Fan 
@Version :   1.0
@Contact :   kellanfan1989@gmail.com
@Desc    :   None
'''

# here put the import lib
import os
import logging
from logging.handlers import RotatingFileHandler
import platform
import json
import etcd
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart

class Mail(object):
    def __init__(self, receivers, subject, content, xlsx_path, xlsx_name_list,logger):
        self.sender = 'fankai@yunify.com'
        self.receivers = receivers
        self.subject = subject
        self.content = content
        self.xlsx_path = xlsx_path
        self.xlsx_name_list = xlsx_name_list
        self.logger = logger
        self.msg = self.__create_mail()

    def add_excel(self,xlsx_name):#添加excel附件
        xlsx_file = self.xlsx_path + xlsx_name
        # 将xlsx文件作为内容发送到对方的邮箱读取excel，rb形式读取，对于MIMEText()来说默认的编码形式是base64 对于二进制文件来说没有设置base64，会出现乱码
        msg_xlsx = MIMEText(open(xlsx_file, 'rb').read(), 'base64', 'utf-8')
        # 设置文件在附件当中的名字
        msg_xlsx.add_header('Content-Disposition', 'attachment', filename=xlsx_name) 
        return msg_xlsx

    def __create_mail(self):
        try:
            main_msg = MIMEMultipart()
            msg = MIMEText(self.content, 'html', 'utf-8') #默认为plain
            main_msg['From'] = formataddr(['',self.sender])
            main_msg['To'] = formataddr(['',','.join(self.receivers)])
            main_msg['Subject'] = self.subject
            main_msg.attach(msg)

            for xlsx_name in self.xlsx_name_list:
                msg_xlsx = self.add_excel(xlsx_name)
                main_msg.attach(msg_xlsx)
        except Exception as e:
            self.logger.error('邮件创建失败！:[{}]'.format(e))
            main_msg = None
        return main_msg
    
    def get_receiver(self):
        return self.receivers

class Mailsender(object):
    def __init__(self,logger):
        self.mail_info = self.__get_info()
        self.logger = logger

    def __get_info(self):
        etc_client = etcd.Client(host='192.168.1.2', port=2379)
        etc_result = etc_client.read('/python/info/yunifymail')
        return json.loads(etc_result.value)

    def send(self,mail):
        ret = True
        try:
            mail_server = smtplib.SMTP(self.mail_info['host'],self.mail_info['port'])
            mail_server.login(self.mail_info['sender'], self.mail_info['pass'])
            mail_server.sendmail(self.mail_info['sender'], mail.get_receiver(), mail.msg.as_string())
            mail_server.quit()
        except Exception as e:
            self.logger.error("发送邮件失败：[{}]".format(e))
            ret = False
        return ret

def create_logger(log_name='spider'):
    if platform.system() == 'Linux':
        log_path = '/var/log/spider'
    elif platform.system() == 'Windows':
        log_path = 'C:\\log\\spider'
    else:
        log_path = None
    # make sure the log dir exist
    if not os.path.exists(log_path):
        os.makedirs(log_path)
    #create format
    fmt = '%(asctime)s.%(msecs)d %(levelname)s %(process)d-%(thread)d: %(message)s (%(filename)s:%(lineno)d)'
    datefmt = '%Y-%m-%d %H:%M:%S'
    formatter = logging.Formatter(fmt, datefmt)
    # create file handler
    log_file = log_path + '/' + log_name + '.log'
    fh = RotatingFileHandler(log_file, mode='a', maxBytes=100000000, backupCount=10, encoding='utf-8')
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(formatter)

    # create logger
    logger = logging.getLogger(log_name)
    if not logger.handlers:
        logger.setLevel(logging.DEBUG)
        logger.addHandler(fh)
    return logger

def main():
    logger = create_logger()
    content = '请查收!谢谢!'
    receivers = ['liuhong@yunify.com']
    subject = '升级L3信息'
    xlsx_path = 'C:\\Users\\Administrator\\Desktop\\'
    xlsx_name_list = ['工单客户需求和bug问题汇总.xlsx', '升级L3工单统计.xlsx']
    mail = Mail(receivers, subject, content, xlsx_path, xlsx_name_list, logger)

    sender = Mailsender(logger)
    ret = sender.send(mail)
    if ret:
        logger.info('[{}] 邮件发送成功！'.format(subject))
    else:
        logger.error('[{}] 邮件发送失败！'.format(subject))

if __name__ == "__main__":
    main()