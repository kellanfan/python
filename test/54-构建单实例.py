# pylint: disable=no-member
# -*- encoding: utf-8 -*-
'''
@File    :   54-构建单实例.py
@Time    :   2019/06/24 11:21:46
@Author  :   Kellan Fan 
@Version :   1.0
@Contact :   kellanfan1989@gmail.com
@Desc    :   None
'''

# here put the import lib
class People(object):
    _flag = None
    def __new__(cls, *args, **kwargs):
        print('new type')
        if not cls._flag:
            cls._flag = super().__new__(cls)
        return cls._flag
    def __init__(self, name, age):
        print('init type')
        self.name = name
        self.age = age

aa = People('aa',12)
bb = People('bb',16)
print(aa.name)
print(bb.name)