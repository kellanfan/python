#!/usr/bin/python
# -*- coding: UTF-8 -*-

import urllib2

def gethtml(url):
    page = urllib2.urlopen(url)
    html = page.read()
    return html

url = raw_input("your url: ")
print gethtml(url)
