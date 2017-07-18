#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Tue 18 Jul 2017 08:32:38 PM CST

# File Name: multipro-2.py
# Description:

"""

import os, urllib2
from multiprocessing import Pool
urllist = ['http://www.jianshu.com/u/347ae48e48e3', 'https://stackedit.io/', 'http://man.chinaunix.net/develop/rfc/RFC4.txt', 'http://dockone.io/', 'http://theme-next.iissnan.com/']
def getcode(url):
    header = {
    'user-agent': ('Mozilla/5.0 (Windows NT 6.2; WOW64)'
                   'AppleWebKit/537.36 (KHTML, like Gecko)'
                   'Chrome/56.0.2924.87 Safari/537.36'),
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    }
    req = urllib2.Request(url, headers = header)
    code = urllib2.urlopen(req).getcode()
    print '[\033[1;35m%s\033[0m] is ok, process is [\033[1;35m%s\033[0m]' %(url, os.getpid())

print 'Parent process %s.' % os.getpid()
l = len(urllist)
p = Pool(l)
for url in urllist:
    p.apply_async(getcode, args=(url,))
p.close()
p.join()
print "All subprocesses done"
