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
        b = list_a[l_list_a].split('|')[1]
        sum_list.append(b)
        l_list_a += 1
    return sum_list

def _mergedict(fdict):
    sum_dict = {}
    for j in fdict:
        url = 'http://m.weather.com.cn/data3/city%s.xml\n' %fdict[j]
        branch_dict = _list2dict(url)
        sum_dict = dict(sum_dict, **branch_dict)
    return sum_dict

url = 'http://m.weather.com.cn/data5/city.xml'
fitst_level_city = _list2dict(url)
second_level_city = _mergedict(fitst_level_city)
city_dict = _mergedict(second_level_city)
city_json = json.dumps(city_dict)
f = file('cityaa.json', 'w')
f.write('city_dict = ')
f.write(city_json)
f.close()
#def getcode(cityname):
#    import sys
#    reload(sys)
#    sys.setdefaultencoding('utf-8')
#    cityname_code = cityname.encode('utf-8')
#    print cityname_code
#    city_code = city_dict.get('cityname_code',-1)
#    print city_code
#    citycode_url =  'http://m.weather.com.cn/data3/city%s.xml' % city_code
#    print citycode_url
#    city_result = _gethtml(citycode_url)
#    print city_result
#    citycode = city_result.split('|')[1]
#    return citycode

