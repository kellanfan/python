#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Mon 01 Apr 2019 11:02:22 AM CST

# File Name: 09-urllib2_proxyhandler.py
# Description:

"""

import urllib2

proxy_switch = True
httpproxy_handler = urllib2.ProxyHandler({"http":"221.6.32.214:50514"})
nullproxy_handler = urllib2.ProxyHandler({})
#如果是私密代理，就需要账户密码，这个时候的写法是{"http": "<username>:<passwd>@代理ip:port"}
#为了私密性，一般账户密码可以写到某个文件，或者环境变量中
#如果写入到环境变量中可以使用os.environ.get()来获取相关变量值，这样比较安全
if proxy_switch:
    opener = urllib2.build_opener(httpproxy_handler)
else:
    opener = urllib2.build_opener(nullproxy_handler)
#构建了一个全局的opener，之后所有的请求都可以用urlopen()方式去发送，也附带Handler的功能
#如果是多次发送请求，建议构建
urllib2.install_opener(opener)
request = urllib2.Request("http://www.baidu.com/")
response = urllib2.urlopen(request)
print response.read()
