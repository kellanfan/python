# pylint: disable=no-member
# -*- encoding: utf-8 -*-
'''
@File    :   class_pra.py
@Time    :   2019/05/13 11:49:26
@Author  :   Kellan Fan 
@Version :   1.0
@Contact :   kellanfan1989@gmail.com
@Desc    :   None
'''

# here put the import lib


class Programer(object):
    def __init__(self, name, age):
        self.name = name
        if isinstance(age, int):
            self.age = age
        else:
            raise Exception('age must be int')

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
    print(p1 == p2)
    print(p1 + p2)
    print(p.name)
