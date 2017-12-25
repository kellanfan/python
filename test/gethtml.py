#!/usr/bin/python
# -*- coding: UTF-8 -*-

import urllib2
def getreq(url):
    header = {
        'user-agent': ('Mozilla/5.0 (Windows NT 6.2; WOW64)'
                       'AppleWebKit/537.36 (KHTML, like Gecko)'
                       'Chrome/56.0.2924.87 Safari/537.36'),
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    }
    req = urllib2.Request(url, headers = header)
    return req
def gethtml(url):
    page = urllib2.urlopen(url)
    html = page.read()
    with open('html', 'w') as f:
        f.write(html)
    return html

url = raw_input("your url: ")
req = getreq(url)
print gethtml(req)
