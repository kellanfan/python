#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Mon 18 Feb 2019 09:31:23 PM CST

# File Name: 10-生成二维码.py
# Description:

"""
import qrcode 

def make_qr(msg):
    qr = qrcode.QRCode(     
        version=1,     
        error_correction=qrcode.constants.ERROR_CORRECT_L,     
        box_size=10,     
        border=4, 
    ) 
    qr.add_data(msg) 
    qr.make(fit=True)  
    img = qr.make_image()
    img.save('123.png')
    print "make pic [123.png] successful..."

if __name__ == '__main__':
    msg = raw_input("请输入信息: ")
    make_qr(msg)
