#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Programer(object):
    def __init__(self, name, age):
        self.name = name
        if isinstance(age, int):
            self.age = age
        else:
            return Exception('age must be int')

    def __eq__(self, other):
        if isinstance(other, Programer):
            if self.age == other.age:
                return True
            else:
                return False
        else:
            return Exception('the type of object must be Programer!')


    def __add__(self, other):
        if isinstance(other, Programer):
            age = self.age + other.age
            return age
        else:
            return Exception('the type of object must be Programer!')
    def __getattribute__(self, name):
        #return getattr(self, name)
        #retrun self.__dict__(name)
        return super(Programer, self).__getattribute__(name)

    def __setattr__(self, name, value):
        #setattr(self, name, value)
        self.__dict__[name] = value


if __name__ == '__main__':
    p = Programer('Allan', 23)
    p1 = Programer('Kellan', 25)
    p2 = Programer('huan', 24)
    print p1 == p2
    print p1 + p2
    print p.name
