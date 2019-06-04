# pylint: disable=no-member
# -*- encoding: utf-8 -*-
'''
@File    :   lirun_answer.py
@Time    :   2019/06/04 15:36:49
@Author  :   Kellan Fan 
@Version :   1.0
@Contact :   kellanfan1989@gmail.com
@Desc    :   None
'''

# here put the import lib
 
i = int(input('净利润:'))
arr = [1000000,600000,400000,200000,100000,0]
rat = [0.01,0.015,0.03,0.05,0.075,0.1]
r = 0
for idx in range(0,6):
    if i>arr[idx]:
        r+=(i-arr[idx])*rat[idx]
        print("此阶段利润：%d " %((i-arr[idx])*rat[idx]))
        i=arr[idx]
print(r)
