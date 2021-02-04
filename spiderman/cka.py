# pylint: disable=no-member
# -*- encoding: utf-8 -*-
'''
@File    :   cka.py
@Time    :   2021/02/04 11:13:59
@Author  :   Kellan Fan 
@Version :   1.0
@Contact :   kellanfan1989@gmail.com
@Desc    :   None
'''

# here put the import lib
import yaml
import platform
from pathlib import Path
from misc.openurl import OpenUrl
from lxml import etree
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

def get_price():
    ourl = OpenUrl('https://training.linuxfoundation.cn/certificate/details/1')
    code,html = ourl.run()
    if code==200:
        selecter = etree.HTML(html)
        try:
            tmp = str(selecter.xpath('//span[@class="text-red mr-2 text-sm"]/text()')[0])

            return int(float(tmp.replace(',','')))
        except:
            return None

def comp(current_price):
    stand_price = 2088
    if current_price:
        if current_price < stand_price:
            return True
    return False


def send_mail(current_price):
    if platform.system() == 'Windows':
        curdir = Path.cwd() / 'python/spiderman'
    elif platform.system() == 'Linux':
        curdir = Path.cwd()

    with open(curdir/'mail.yaml') as f:
        conf = yaml.safe_load(f.read())
    sender = conf.get('sender')
    my_pass = conf.get('pass')
    receiver = conf.get('receiver')
    ret=True
    try:
        msg = MIMEText('当前价格为[{}]'.format(current_price), 'html', 'utf-8')
        msg['From'] = formataddr(['', sender])
        msg['To'] = formataddr(['', receiver])
        msg['Subject']="CKA考试降价啦!"
        server=smtplib.SMTP_SSL("smtp.qq.com", 465)
        server.login(sender, my_pass)
        server.sendmail(sender, [receiver,], msg.as_string())
        server.quit()  
    except Exception as e:
        print(e)
        ret=False
    return ret
 
def main():
    current_price = get_price()
    if comp(current_price):
        if send_mail(current_price):
            print('send mail successful')
        else:
            print('send mail failed')

if __name__ == '__main__':
    main()