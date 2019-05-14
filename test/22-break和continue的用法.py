# pylint: disable=no-member
# -*- encoding: utf-8 -*-
'''
@File    :   break-continue.py
@Time    :   2019/05/13 10:18:31
@Author  :   Kellan Fan 
@Version :   1.0
@Contact :   kellanfan1989@gmail.com
@Desc    :   熟悉break和continue的使用方法。break是直接退出循环，而continue是跳过本次循环
'''

# here put the import lib


i=0
for i in range(5):
    i += 1
    for j in range(3):
        if j ==1:
            print("退出循环")
            break
        print("this j is %d" %j)
    for h in range(3):
        if h ==1:
            print("跳过本次循环")
            continue
        print("the h is %d" %h)
    print("the i is %d" %i)
