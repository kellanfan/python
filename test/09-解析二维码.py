#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Mon 18 Feb 2019 08:39:38 PM CST

# File Name: wechat-login.py
# Description:

"""
from PIL import Image
import zbarlight

def get_QR(pic):
    img = Image.open(pic)
    code_message = zbarlight.scan_codes('qrcode', img)[0].decode('utf-8')
    return code_message

if __name__ == '__main__':
    qrdata= get_QR('123.png')
    print(qrdata)   
