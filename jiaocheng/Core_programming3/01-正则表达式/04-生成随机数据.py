#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Mon 18 Dec 2017 08:26:04 PM CST

# File Name: 03-生成随机数据.py
# Description:

"""

from random import randrange, choice
from string import ascii_lowercase as lc #这个会返回小写的a-z
#from sys import maxint 64位系统的maxint数值超过了2的32次方
from time import ctime

tlds = ('com', 'cn', 'net', 'edu', 'org', 'gov')
f = open('redata.txt','w')
for i in xrange(randrange(5, 11)): #控制整体生成的数据量
    dtint = randrange(2**32) 
    dtstr = ctime(dtint) #将数值转换成响应的时间
    llen = randrange(4,8) #生成随机数
    login = ''.join(choice(lc) for j in range(llen)) #随机选择4-8个字符串加到空字符串中
    dlen = randrange(llen, 15)
    dom = ''.join(choice(lc) for j in range(dlen)) #同理
    print  "%s::%s@%s.%s::%d-%d-%d" %(dtstr, login, dom, choice(tlds), dtint, llen, dlen)
    f.write("%s::%s@%s.%s::%d-%d-%d\n" %(dtstr, login, dom, choice(tlds), dtint, llen, dlen))
f.close()
