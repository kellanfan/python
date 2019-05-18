# pylint: disable=no-member
# -*- encoding: utf-8 -*-
'''
@File    :   weather.py
@Time    :   2019/05/13 12:19:51
@Author  :   Kellan Fan 
@Version :   1.0
@Contact :   kellanfan1989@gmail.com
@Desc    :   None
'''

# here put the import lib
import requests
import json
from city_code import city

cityname = input("你想查那个城市的天气？ ")
citycode = city.get(cityname)
if citycode:
    try:
        url = 'http://www.weather.com.cn/data/cityinfo/%s.html' %citycode
        doc = requests.get(url)
        data = json.loads(doc.content)
        result = data['weatherinfo']
        str_temp = ('%s\n%s ~ %s') %(result['weather'],result['temp1'],result['temp2'])
        print(str_temp)
    except:
        print("查询失败！")
else:
    print("没有该城市：%s" %cityname)
