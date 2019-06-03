# pylint: disable=no-member
# -*- encoding: utf-8 -*-
'''
@File    :   classh1.py
@Time    :   2019/06/03 15:20:14
@Author  :   Kellan Fan 
@Version :   1.0
@Contact :   kellanfan1989@gmail.com
@Desc    :   None
'''

# here put the import lib

class Student(object):
    def __init__(self, sco):
        self._score = sco

    @property #python内置的装饰器负责把一个方法变成属性调用，把一个getter方法变成属性，只需要加上@property就可以了
    def score(self):  #定义了一个getter方法
        return self._score

    @score.setter   #@property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
if __name__ == "__main__":
    a=Student(50)
    print(a.score)
    a.score = 80
    print(a.score)