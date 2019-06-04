# pylint: disable=no-member
# -*- encoding: utf-8 -*-
'''
@File    :   dingzhiclass.py
@Time    :   2019/06/04 14:45:59
@Author  :   Kellan Fan 
@Version :   1.0
@Contact :   kellanfan1989@gmail.com
@Desc    :   类的str方法
'''

# here put the import lib

class Student(object):
    def __init__(self, name):
        self.name = name

class Student_str(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student object (name: %s)' %self.name
if __name__ == "__main__":
    print(Student('kellan'))
    print(Student_str('kellan'))