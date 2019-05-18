# pylint: disable=no-member
# -*- encoding: utf-8 -*-
'''
@File    :   bloomsearch.py
@Time    :   2019/05/13 10:06:15
@Author  :   Kellan Fan 
@Version :   1.0
@Contact :   kellanfan1989@gmail.com
@Desc    :   布隆过滤器,可参考链接：https://www.cnblogs.com/zhxshseu/p/5289871.html
'''

# here put the import lib

class Bloomfilter(object):
    def __init__(self,size):
        self.values = [False] * size
        self.size = size

    def __hash_value(self, value):
        return hash(value) % self.size

    def add_value(self, value):
        h = self.__hash_value(value)
        self.values[h] = True

    def might_contain(self, value):
        h = self.__hash_value(value)
        return self.values[h]

    def print_contents(self):
        print(self.values)

if __name__ == '__main__':
    bf = Bloomfilter(12)
    bf.add_value(12)
    print(bf.might_contain(12))