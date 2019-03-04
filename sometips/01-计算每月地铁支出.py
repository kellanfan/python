#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Tue 26 Feb 2019 11:25:32 AM CST

# File Name: 01-计算每月地铁支出.py
# Description: 据北京市发改委网站消息称，北京市将从2015年12月28起实施公共交通新票价：
地铁6公里(含)内3元，公交车10公里(含)内2元，使用市政交通卡通刷卡乘公交车普通卡5折，学生卡2.5折。
具体实施方案如下：
1、城市公共电汽车价格调整为：10公里(含)内2元，10公里以上部分，每增加1元可乘坐5公里。使用市政交通卡通刷卡乘坐城市公共电汽车，市域内路段给予普通卡5折，学生卡2.5折优惠;市域外路段维持现行折扣优惠不变。享受公交政策的郊区客运价格，由各区、县政府按照城市公共电汽车价格制定。
2、轨道交通价格调整为：6公里(含)内3元;6公里至12公里(含)4元;12公里至22公里(含)5元;22公里至32公里(含)6元;32公里以上部分，每增加1元可乘坐20公里。使用市政交通卡通刷卡乘坐轨道交通，每自然月内每张卡支出累计满100元以后的乘次，价格给予8折优惠;满150元以后的乘次，价格给予5折优惠;支出累计达到400元以后的乘次，不再享受打折优惠。
要求：假设每个月，小明都需要上20天班，每次上班需要来回1次，即每天需要乘坐2次同样路线的地铁；每月月初小明第一次刷公交卡时，扣款5元；编写程序，帮小明完成每月乘坐地铁需要的总费用

"""
import sys
#这里假设小明上班只乘坐地铁，和公交车无关

def subway(distance):
    cost = 0
    day = 1
    distance = int(distance)
    while day <= 40:
        if cost >= 100 and cost < 150:
            rate = 0.8
        elif cost >= 150 and cost < 400:
            rate = 0.5
        else:
            rate = 1


        if distance == 0:
            print("不上班吗")
            sys.exit()
        elif distance <= 6 and distance > 0:
            cost += (3*rate)
        elif distance <= 12 and distance > 6:
            cost += (4*rate)
        elif distance <= 22 and distance > 12:
            cost += (5*rate)
        elif distance <= 32 and distance > 22:
            cost += (6*rate)
        elif distance > 32:
            if (distance - 32)%20 == 0:
                cost +=((6+(distance-32)/20)*rate)
            else:
                cost +=((6+(distance-32)/20+1)*rate)

        day += 1
    return cost

if __name__ == '__main__':
    distance = input("请输入距离: ")
    cost = subway(distance)
    print("每月的总消费为: %d"%cost)
