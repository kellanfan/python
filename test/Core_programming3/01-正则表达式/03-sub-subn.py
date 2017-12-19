#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Mon 18 Dec 2017 10:55:19 AM CST

# File Name: 03-sub-subn.py
# Description:

"""

import re
#将X替换成Mr. Smith
print re.sub('X', 'Mr. Smith', 'attn: X\n\nDear X,\n')
print re.subn('X', 'Mr. Smith', 'attn: X\n\nDear X,\n')

#将日期格式MM/DD/YY{,YY}换成DD/MM/YY{,YY}
print re.sub(r'(\d{1,2})/(\d{1,2})/(\d{2}|\d{4})', r'\2/\1/\3', '2/20/17')
print re.sub(r'(\d{1,2})/(\d{1,2})/(\d{2}|\d{4})', r'\2/\1/\3', '2/20/2017')
