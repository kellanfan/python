#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Fri 22 Mar 2019 05:04:28 PM CST

# File Name: 01-urllib2_urlopen.py
# Description:

"""
import urllib2
#User-Agent必须要有，这是反爬虫的第一步
header = {"User-Agent":"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}
#通过Request构造一个请求对象
request = urllib2.Request("http://www.baidu.com", headers = header)
#向指定的url地址发送请求，并返回服务器响应的类文件对象
response = urllib2.urlopen(request)
#服务器返回的类文件对象支持python文件对象的操作方法
#read方法就是读取文件里的全部内容，返回字符串
html = response.read()
#打印响应
print html
print "="*20
#HTML响应码
print response.getcode()
print "="*20
#返回实际数据的实际URL，防止重定向问题
print response.geturl()
print "="*20
#返回服务器响应的HTTP报头
print response.info()
print "="*20
