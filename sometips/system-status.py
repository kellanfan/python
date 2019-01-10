#/usr/bin/env python
#-*- coding:utf-8 -*-
"""
# Author: kellanfan
# Created Time : Thu 14 Sep 2017 10:54:42 PM CST

# File Name: system-status.py
# Description: 利用psutil模块实现系统监控，分析和限制系统资源及进程的管理。监控有个dstat命令，是使用python编写，可以使用，并且看下源码。这个脚本就只是显示相关信息就可以了
"""


import psutil
def print_col(info):
    print "\033[1;35m" 
    print info
    print "\033[0m!"

def sys_cpu(percpu):
    if percpu == 0:
        print_col(psutil.cpu_times().user)
    elif percpu == 1:
        i = 0
        for c in psutil.cpu_times(percpu=True):
            print "CPU编号：%s" %i
            print "     用户比：%s" %c.user
            i += 1

sys_cpu(0)
sys_cpu(1)
