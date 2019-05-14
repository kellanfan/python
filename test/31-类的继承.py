#!/usr/bin/python
#coding=utf-8

class School(object):
    def __init__(self, sname):
        self.sname = sname
    def ps(self):
        print("i\'m in the %s school" %self.sname)

class Student(School):

    def __init__(self, sname, name, score): #私有方法，同样不能直接调用
        self.__name = name #加双下划线表示私有属性，在外面不能直接调用，只能对象内调用
        self.__score = score
        School.__init__(self,sname)
    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score

    def set_score(self, score):
        if not isinstance(score, int):
            raise ValueError('score must be int!')
        if score < 0 or score > 100:
            raise ValueError('score must between 0 and 100')
    def ps1(self):
        print("I\'m in %s , and my name is %s" %(self.sname, self.__name))

class Teacher(object):
    def ps(self):
        print("i\'m not in School class and Student Class,but i have ps")
    def ps1(self):
        print("i\'m not in School class and Student Class,but i have ps1")

def f(x):
    x.ps()
    x.ps1()

    
f(Student('hengshui','kellan','100'))
f(Teacher())
