#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Fri 12 Oct 2018 10:28:23 AM CST

# File Name: 01-resuests添加header和参数.py
# Description:

"""
import requests
kw = {'wd':'长城'}
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

response = requests.get('http://www.baidu.com/s?', params=kw, headers=headers)
print(response.text)
print(response.content)
print(response.url)
print(response.encoding)
print(response.status_code)
