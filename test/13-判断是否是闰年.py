#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Sun 10 Mar 2019 11:43:46 AM CST

# File Name: 13-判断是否是闰年.py
# Description: 闰年判定方法：能被400整除。或者能被4整除但不能被100整除

"""
def is_Runnian(year):
    if year%4 == 0 and year%100 != 0:
        return True
    else:
        return False

def main():
    i_year = input("请输入年份: ")
    if is_Runnian(int(i_year)):
        print("%s 是闰年"%i_year)
    else:
        print("%s 不是闰年"%i_year)

if __name__ == '__main__':
    main()
        
