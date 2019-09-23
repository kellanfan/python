#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Wed 05 Jul 2017 02:59:09 PM CST

# File Name: test.py
# Description:

"""

import re
from openurl import OpenUrl
url = 'https://www.piaohua.com/html/kehuan/2012/0329/24007.html'
ourl = OpenUrl(url)
code, content = ourl.openurl()
reg = re.compile(r'<a href="(ftp:.+?)">')
if code == 200:
    l = re.findall(reg, content)
    print(l)
