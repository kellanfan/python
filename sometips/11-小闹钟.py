# pylint: disable=no-member
# -*- encoding: utf-8 -*-
'''
@File    :   11-小闹钟.py
@Time    :   2019/05/21 11:26:50
@Author  :   Kellan Fan 
@Version :   1.0
@Contact :   kellanfan1989@gmail.com
@Desc    :   None
'''

# here put the import lib

import datetime
import time
import sys
from  multiprocessing import Pool

def str2int(x):
    return int(x)

def naozhong(date,timer):
    #先对得到的时间进行格式化处理
    year, month, day = map(str2int, date.split('-'))
    hour, minute, second = map(str2int, timer.split(':'))
    #检查输入是否正确
    if month in range(1,13) and day in range(1,32) and hour in range(0,24) and minute in range(0,60) and second in range(0,60):
        wake_time = datetime.datetime(year, month, day, hour, minute, second)
        #进入死循环，开始倒计时
        while True:
            #判断时间是否现在时间之前的时间
            if (wake_time - datetime.datetime.now()).days < 0:
                print("时间是之前的，无法设定！！！")
                break
            #获取差值
            dvalue = (wake_time - datetime.datetime.now()).seconds
    
            if dvalue <= 0:
                print('it is time!!!')
                break
            time.sleep(1)
    else:
        print("格式错误，请输入正确时间！！！")
        sys.exit(1)

def main():
    if len(sys.argv) != 3:
        print(
"""
Usage:
    naozhong <YYYY-MM-DD> <HH:MM:SS>
Example:
    naozhong 2018-02-14 12:12:12
""")
        sys.exit(2)

    date = sys.argv[1]
    timer = sys.argv[2]
    p = Pool(10)
    p.apply_async(naozhong, (date,timer))
    p.close()
    p.start()

if __name__ == '__main__':
    main()
