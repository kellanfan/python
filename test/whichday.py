#!/usr/bin/python
# -*- coding: UTF-8 -*-

date = raw_input("需要查询的时间 eg:1999-01-01: ")
def form(date):
    list = date.split('-')
    return list

s = form(date)
year = int(s[0])
month = int(s[1])
day = int(s[2])
months = (0, 31, 59, 90,120,151,181,212,243,273,304,334)
if 0 < month <= 12 or 0 < day <= 31:
    sum = months[month -1]
else:
    print "Error: date Error"

sum += day
leap = 0
if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
    leap = 1
if (leap == 1) and (month > 2):
    sum += 1
print 'it is the %dth day.' % sum
