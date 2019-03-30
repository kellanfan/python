#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Wed 27 Mar 2019 12:00:43 PM CST

# File Name: 05-urllib_post.py
# Description:
    已经改成api了，无法访问，这里只是模拟下post请求
"""

import urllib
import urllib2
key = raw_input("请输入需要翻译的信息：")
headers = {
	"Accept": "application/json, text/javascript, */*; q=0.01",
	"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
	"User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
	"X-Requested-With": "XMLHttpRequest"
}
#发送到url的表单数据
formdata={
"i": key,
"from": "AUTO",
"to": "AUTO",
"smartresult": "dict",
"client": "fanyideskweb",
"salt": "15536590504619",
"sign": "fe2224625d86bd48dbe1a5f32df292b0",
"ts": "1553659050461",
"bv": "f8c295588ce195d0453511f751132244",
"doctype": "json",
"version": "2.1",
"keyfrom": "fanyi.web",
"action": "FY_BY_REALTlME",
"typoResult": "false"
}
data = urllib.urlencode(formdata)
#真正的url
url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
#如果Request的data有数据就是post请求，没有数据就是get请
request = urllib2.Request(url, data=data, headers = headers)
print urllib2.urlopen(request).read()
