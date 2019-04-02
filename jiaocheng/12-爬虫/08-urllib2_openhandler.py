#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Mon 01 Apr 2019 10:24:02 AM CST

# File Name: 08-urllib2_openhandler.py
# Description:

"""
import urllib2

#构建一个HTTPHandler处理器对象，支持处理HTTP请求
#开启debug log模式，程序会自动打印收发包请求信息
http_handler = urllib2.HTTPHandler(debuglevel=1)
#调用build_opener()方法构建一个自定义的opener对象，参数是构建的处理器对象
opener = urllib2.build_opener(http_handler)

request = urllib2.Request("http://www.baidu.com/")
response = opener.open(request)
print response
