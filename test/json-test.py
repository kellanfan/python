#!/usr/bin/python
# -*- coding: UTF-8 -*-

import json
import urllib2
url_org = 'http://m.weather.com.cn/data5/city.xml'
def gethtml(url):
    page = urllib2.urlopen(url)
    html = page.read()
    return html

first_level_html = gethtml(url_org)
first_level_list = []
for s in first_level_html:
    first_level_list.append(s)
first_level_dict = json.dumps(first_level_list)

print first_level_dict
