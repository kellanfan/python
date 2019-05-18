# pylint: disable=no-member
# -*- encoding: utf-8 -*-
'''
@File    :   whichday.py
@Time    :   2019/05/13 08:38:36
@Author  :   Kellan Fan 
@Version :   1.0
@Contact :   kellanfan1989@gmail.com
@Desc    :   判断输入的日期是一年中的第几天
'''

# here put the import lib
import datetime
import sys

if __name__ == '__main__':
    date = input("需要查询的时间 eg:1999-01-01: ")
    try:
        list = date.split('-')
        year,month,day = map(int, list)
    except ValueError as e:
        print("Error: %s"%e)
        sys.exit()
    try:
        end_day = datetime.datetime(year,month,day)
    except ValueError as e:
        print("Error: %s"%e)
        sys.exit()
    first_day = datetime.datetime(year,1,1)
    t= (end_day - first_day).days
    print("It is the %dth day."%t)