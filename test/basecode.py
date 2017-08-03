#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Wed 02 Aug 2017 07:28:56 PM CST

# File Name: basecode.py
# Description: 如果要编码的二进制数据不是3的倍数，最后会剩下1个或2个字节怎么办？Base64用\x00字节在末尾补足后，再在编码的末尾加上1个或2个=号，表示补了多少字节，解码的时候，会自动去掉。

"""

import base64

l = 'sdfqwerzxc'
el = base64.b64encode(l)
print "the encode is %s.." %el
a = el.split('=')[0]
print "the code is %s.." %a
for i in range(10):
    cnum = 4 * i - len(a)
    if cnum > 0:
        ls = '=' * cnum
        al = a + ls
        break
deal = base64.b64decode(al)
print "the decode is %s.." %deal
        
print base64.b64encode('i\xb7\x1d\xfb\xef\xff')
print base64.urlsafe_b64encode('i\xb7\x1d\xfb\xef\xff')
