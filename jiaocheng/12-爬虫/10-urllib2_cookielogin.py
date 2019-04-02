#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Mon 01 Apr 2019 01:43:18 PM CST

# File Name: 10-urllib2_cookielogin.py
# Description:

"""
import urllib
import urllib2
import cookielib
#通过cookieJar创建一个存储cookie值的对象
cookie = cookielib.CookieJar()
#构造处理器对象，用来处理cookie，
cookie_handler = urllib2.HTTPCookieProcessor(cookie)
#构建一个自定义的opener
opener = urllib2.build_opener(cookie_handler)
#通过这个参数直接添加headers
opener.addheaders = [("User-Agent", "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36")]
url = "http://www.renren.com/PLogin.do"
data = {"username":"","password":""}
data = urllib.urlencode(data)
#第一次是post请求，发送登陆需要的参数，获取cookie
request = urllib2.Request(url,data=data)
#发送post请求，生成登陆后的cookie
response = opener.open(request)

print response.read()
#第二次请求可以是get请求，这个请求将保存cookie一并发送给服务器，
request1 = opener.open("http://www.renren.com/11111")
print response1.read()
