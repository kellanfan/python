#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import openpyxl, time, datetime
from exec_psql import select_sql
import os
import calendar as cal
def month_last_day():
    '''获取最近3个月的日期'''
    today = datetime.date.today()
    year = today.year
    month = today.month
    day = today.day
    if day not in range(28,32): #此处判断不是很准确
        if month == 1:
            month = 12
            year = year - 1
        else:
            month = month - 1
        print "今天是%s号，获取之前3个月的数据，不含本月..."% str(day)
    if month == 1:
        last_year = year - 1
        last_date = str(last_year) + '-12-' + str(cal.monthrange(last_year, 12)[1])
        l_last_date = str(last_year) + '-11-' + str(cal.monthrange(last_year, 11)[1])
    elif month == 2:
        last_year = year - 1
        last_date = str(year) + '-01-' + str(cal.monthrange(year, 01)[1])
        l_last_date = str(last_year) + '-12-' + str(cal.monthrange(last_year, 12)[1])
    else:
        last_year = year
        last_date = str(last_year) + '-' + str(month-1) + '-' + str(cal.monthrange(year, month-1)[1])
        l_last_date = str(last_year) + '-' + str(month-2) + '-' + str(cal.monthrange(year, month-2)[1])

    now_date = str(year) + '-' + str(month) + '-' + str(cal.monthrange(year, month)[1])
    return l_last_date,last_date,now_date

def yesterday():
    '''获取昨天的日期'''
    today = datetime.date.today()
    oneday = datetime.timedelta(days=1)
    return today-oneday

if __name__ == '__main__':
    date_list = month_last_day()
    for date in date_list:
        cmd = 'select zone,hyper_type,used_vdisk,sign_time from infomation where sign_time = \'%s\'' % date
        content = select_sql(cmd)
        for cont in content:
            print cont
