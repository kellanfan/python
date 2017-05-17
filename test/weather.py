#!/usr/bin/python
# -*- coding: UTF-8 -*-

import urllib2
import json
from city_code import city
cityname = raw_input("你想查那个城市的天气？ ")
citycode = city.get(cityname)
if citycode:
    try:
        url = 'http://www.weather.com.cn/data/cityinfo/%s.html' %citycode
        content = urllib2.urlopen(url).read()
        data = json.loads(content)
        result = data['weatherinfo']
        str_temp = ('%s\n%s ~ %s') %(result['weather'],result['temp1'],result['temp2'])
        print str_temp
    except:
        print "查询失败！"
else:
    print "没有该城市：%s" %result['city']
