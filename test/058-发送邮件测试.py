# pylint: disable=no-member
# -*- encoding: utf-8 -*-
'''
@File    :   058-发送邮件测试.py
@Time    :   2020/01/01 10:50:26
@Author  :   Kellan Fan 
@Version :   1.0
@Contact :   kellanfan1989@gmail.com
@Desc    :   None
'''

# here put the import lib
import json
import etcd
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

class Mail(object):
    def __init__(self, receivers, subject, content):
        self.sender = '1107663350@qq.com'
        self.receivers = receivers
        self.subject = subject
        self.content = content
        self.msg = self.__create_mail()

    def __create_mail(self):
        try:
            msg = MIMEText(self.content, 'html', 'utf-8') #默认为plain
            msg['From'] = formataddr(['',self.sender])
            msg['To'] = formataddr(['',','.join(self.receivers)])
            msg['Subject'] = self.subject
        except:
            print('邮件创建失败！')

        return msg
    
    def get_receiver(self):
        return self.receivers

class Mailsender(object):
    def __init__(self):
        self.mail_info = self.__get_info()

    def __get_info(self):
        etc_client = etcd.Client(host='192.168.1.2', port=2379)
        etc_result = etc_client.read('/python/info/qqmail')
        return json.loads(etc_result.value)

    def send(self,mail):
        ret = True
        try:
            mail_server = smtplib.SMTP_SSL(self.mail_info['host'],self.mail_info['port'])
            mail_server.login(self.mail_info['sender'], self.mail_info['pass'])
            mail_server.sendmail(self.mail_info['sender'], mail.get_receiver(), mail.msg.as_string())
            mail_server.quit()
        except Exception as e:
            print(e)
            ret = False
        return ret

def main():
    content = '<h3>hahaha</h3>'
    receivers = ['1107663350@qq.com']
    subject = '测试邮件'
    mail = Mail(receivers, subject, content)

    sender = Mailsender()
    ret = sender.send(mail)
    if ret:
        print('邮件发送成功！')
    else:
        print('邮件发送失败！')

if __name__ == "__main__":
    main()