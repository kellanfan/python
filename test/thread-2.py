#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Wed 19 Jul 2017 07:18:06 PM CST

# File Name: thread-2.py
# Description:

"""
import threading
from time import ctime
import urllib2
urllist = ['http://www.jianshu.com/u/347ae48e48e3', 'https://stackedit.io/', 'http://man.chinaunix.net/develop/rfc/RFC4.txt', 'http://dockone.io/', 'http://theme-next.iissnan.com/']
def getcode(url):
    header = {
    'user-agent': ('Mozilla/5.0 (Windows NT 6.2; WOW64)'
                   'AppleWebKit/537.36 (KHTML, like Gecko)'
                   'Chrome/56.0.2924.87 Safari/537.36'),
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    }
    print 'thread [\033[1;35m%s\033[0m] starting...' % threading.current_thread().name
    req = urllib2.Request(url, headers = header)
    code = urllib2.urlopen(req).getcode()
    print '[\033[1;35m%s\033[0m] is ok... and thread %s ' % (url, threading.current_thread().name)

threads = []
for url in urllist:
    tt = threading.Thread(target=getcode, args=(url,))
    threads.append(tt)
if __name__ == '__main__':
    for t in threads:
#        t.setDaemon(True)
        t.start()
    t.join()
    print "%s Done..." %ctime()
