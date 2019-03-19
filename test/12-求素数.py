#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Sun 10 Mar 2019 11:06:35 AM CST

# File Name: 12-求素数.py
# Description: 求100-200里面的所有素数。素数的特征是除了1和其本身能被整除，其他数都不能被整除

"""
import sys

def is_Sushu(item):
    "判断是否为素数"
    l_item = []
    for i in range(1,item+1):
        if item%i == 0:
            l_item.append(i)

    if len(l_item) == 2 and 1 in l_item and item in l_item:
        return True
    else:
        return False

def main():
    inputs = input("请输入数字范围<100-200>: ")
    try:
        l_inputs = inputs.split('-')
    except:
        print("请输入数字范围<100-200>")
        sys.exit()
    result = []
    first_num = int(l_inputs[0])
    last_num = int(l_inputs[1])
    for i in range(first_num,last_num):
        if is_Sushu(i):
            result.append(i)

    print("[%d-%d] has %d sushu, the list is %s .."%(first_num,last_num,len(result),str(result)))

if __name__ == '__main__':
    main()
