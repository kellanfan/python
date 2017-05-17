#!/usr/bin/python
# -*- coding: UTF-8 -*-
import urllib2
import json
def _gethtml(url):
    page = urllib2.urlopen(url)
    html = page.read()
    return html

def _getlist(url):
    sum_list = []
    list_a = []
    a = _gethtml(url).split(',')
    for s in a:
        list_a.append(s)
    lenth_list_a = len(list_a)
    l_list_a = 0
    while l_list_a < lenth_list_a:
        list_a_a = []
        b = list_a[l_list_a].split('|')[0]
        sum_list.append(b)
        l_list_a += 1
    return sum_list

def _mergelist(flist):
    sum_list = []
    lenth = len(flist)
    l = 0
    while l < lenth:
        url = 'http://m.weather.com.cn/data3/city%s.xml' %flist[l]
        part_list = _getlist(url)
        sum_list.extend(part_list)
        l += 1
    return sum_list
    

url = 'http://m.weather.com.cn/data5/city.xml'
first_city_list = _getlist(url)
second_city_list = _mergelist(first_city_list)
result = 'city = {\n'
for c in second_city_list:
    url1 = 'http://m.weather.com.cn/data3/city%s.xml' %c
    html = _gethtml(url1)
    districts = html.split(',')
    for d in districts:
        name = d.split('|')[1]
        part_code = d.split('|')[0]
        url2 = 'http://m.weather.com.cn/data3/city%s.xml' %part_code
        print url2
        data = _gethtml(url2)
        try:
            code = data.split('|')[1]
        except:
            continue
        line = " '%s': '%s',\n" % (name, code)
        result += line
result += '}'
f = file('city_code.py', 'w')
f.write(result)
f.close()
