# pylint: disable=no-member
# -*- encoding: utf-8 -*-
'''
@File    :   005-原型模式.py
@Time    :   2019/10/18 09:26:16
@Author  :   Kellan Fan 
@Version :   1.0
@Contact :   kellanfan1989@gmail.com
@Desc    :   None
'''

# here put the import lib
import copy
from collections import OrderedDict

class Book(object):
    def __init__(self,name,authors,price,**kwargs):
        self.name = name
        self.authors = authors
        self.price = price
        self.__dict__.update(kwargs) #更新到对象的属性中
    def __str__(self):
        mylist = []
        orderdict = OrderedDict(sorted(self.__dict__.items()))
        for i in orderdict.keys():
            mylist.append('{}: {}'.format(i,orderdict[i]))
            if i == 'price':
                mylist.append('$')
            mylist.append('\n')
        return ''.join(mylist)

class Protopyte(object):
    '''
        实现原型设计模式，关键是clone方法，通过deepcopy深度拷贝
    '''
    def __init__(self):
        self.objects = dict()
    def register(self, identifier, obj):
        self.objects[identifier] = obj
    def unregister(self, identifier):
        del self.objects[identifier]
    def clone(self,identifier,**kwargs):
        found = self.objects.get(identifier)
        if not found:
            raise ValueError('Incorrent object identifier: {}'.format(identifier))
        obj = copy.deepcopy(found)
        obj.__dict__.update(kwargs)
        return obj

def main():
    book1 = Book('Python','kellan',12,publisher='xinhuashe',length=500,public_date='2013-09-21',
        tag=('Python','Programming','Lang'))
    property = Protopyte()
    bid = 'first'
    property.register(bid,book1)
    book2 = property.clone(bid, name='Python acc1',price=14,length=489,public_date='2019-10-10',edition=2)
    for i in (book1, book2):
        print(i)
    print('ID book1: {} != ID book2: {}'.format(id(book1),id(book2)))
if __name__ == "__main__":
    main()