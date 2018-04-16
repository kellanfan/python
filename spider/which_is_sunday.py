#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Mon 16 Apr 2018 09:25:39 AM CST

# File Name: aa.py
# Description:

"""
import datetime
def sunday():
    week_list = []
    year = 17
    for month in range(1,12):
        for day in range(1,31):
            try:
                week = datetime.date.weekday(datetime.date(year,month,day))
            except:
                week = 7
            if week == 6:
                if month < 10:
                    month = '0' + str(month)
                if day < 10:
                    day = '0' + str(day)
                week_date = str(year) + str(month) + str(day)
                week_list.append(week_date)
    
    return week_list


if __name__ == '__main__':
    sunday()
