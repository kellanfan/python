#/usr/bin/env python
#-*- coding:utf-8 -*-
"""
# Author: kellanfan
# Created Time : Tue 12 Sep 2017 05:56:57 PM CST

# File Name: niMingHanShu.py
# Description: 匿名函数 格式  变量 =  lambda 参数：式子   就是变量指向一个匿名函数
调用：变量(参数)
匿名函数 ：的后面式子自带return，所以一般可以理解为
变量 =  lambda 参数：return 式子
因为是这样，所以简单的函数可以用匿名函数，但是复杂的函数还是要使用def定义
"""


def suma(a,b):
    a + b
#没有return就没办法输出返回值
suma(11,22)


#定义匿名函数
func = lambda a,b:a+b
#自带retuen
print func(11,22)



#匿名函数的应用
infors = [{"name":"kellan","age":23},{"name":"haha","age":21},{"name":"zhao","age":22}]

#对上面的列表进行排序，由于元素是字典没办法进行排序，所以只能找出一个key进行排序，这就可以使用到

#按name这个key进行排序，就是把整个字典元素当做参数，返回值是这个字典中指定key的value

infors.sort(key=lambda x:x['name'])
print infors
