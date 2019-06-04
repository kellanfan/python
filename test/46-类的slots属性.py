# pylint: disable=no-member
# -*- encoding: utf-8 -*-
'''
@File    :   ex_slots.py
@Time    :   2019/06/04 15:23:27
@Author  :   Kellan Fan
@Version :   1.0
@Contact :   kellanfan1989@gmail.com
@Desc    :    由于'aa'没有被放到__slots__中，所以不能绑定aa属性，试图绑定aa将得到AttributeError的错误。
            __slots__定义的属性仅对当前类起作用，对继承的子类是不起作用的。
            除非在子类中也定义__slots__，这样，子类允许定义的属性就是自身的__slots__加上父类的__slots__

'''

# here put the import lib

class Student(object):
    __slots__ = ('name', 'age')


class Hstudent(Student):
    pass

if __name__ == "__main__":
    s = Student()
    s.name = 'kellan'
    s.age = 23
    #s.aa = 'ss' 
    g = Hstudent()
    g.aa = 'aa'