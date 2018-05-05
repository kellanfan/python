#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Tue 28 Nov 2017 08:11:04 PM CST

# File Name: 26-异常.py
# Description:

"""
switch = False
try:
    10/0
    print "---1---"
except NameError:
    print "NameError:没有这个名字..."
except IOError:
    print "IOError:文件不存在..."
except Exception:
    if switch:
        print "Exception:所有异常都会匹配这个..."
    else:
        raise #异常中抛出异常，如果有些异常不想在这个层面处理，就往上层抛出
else:
    print "无异常才会执行..."
finally:
    print "不管有无异常，都会执行..."


