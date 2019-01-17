#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Fri 11 Jan 2019 11:31:32 AM CST

# File Name: 03-argparse命令解析模块.py
# Description:

"""
import time
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-a', '--asctime', help='display the time of current time on the asctime mode', action="store_true")
parser.add_argument('-s', '--timestamp', help='display Time stamp of current time', action="store_true")
parser.add_argument('-c', '--chinaform', help='display china form of current time', action="store_true")
args= parser.parse_args()
if args.asctime:
    print time.asctime()
elif args.timestamp:
    print time.time()
elif args.chinaform:
    now=time.localtime()
    print "%s年%s月%s日 %s时%s分%s秒"%(now[:6])
else:
    print time.strftime("%Y-%m-%d %X",time.localtime())
