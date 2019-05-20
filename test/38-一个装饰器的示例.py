# pylint: disable=no-member
# -*- encoding: utf-8 -*-
'''
@File    :   decorator.py
@Time    :   2019/05/17 10:30:31
@Author  :   Kellan Fan 
@Version :   1.0
@Contact :   kellanfan1989@gmail.com
@Desc    :   None
'''

# here put the import lib

import functools

def log(begin_text,end_text):
    def decorate(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print('%s %s()' %(begin_text, func.__name__))
            return func(*args,**kw)
        def wrapper1(*args,**kw):
            print('%s %s()' %(end_text, func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorate

@log('begin','end')
def now():
    print('2017-06-08')
if __name__ == '__main__':
    now()
