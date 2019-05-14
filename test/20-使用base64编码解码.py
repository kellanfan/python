#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Wed 02 Aug 2017 07:28:56 PM CST

# File Name: basecode.py
# Description: 如果要编码的二进制数据不是3的倍数，最后会剩下1个或2个字节怎么办？Base64用\x00字节在末尾补足后，
# 再在编码的末尾加上1个或2个=号，表示补了多少字节，解码的时候，会自动去掉。

"""

import base64

l = input("the str is: ")
el = base64.b64encode(l.encode())
dl = base64.b64decode(el)
print("the encode is %s.." %el.decode())
print("the decode is %s.." %dl.decode())