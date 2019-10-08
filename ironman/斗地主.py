# pylint: disable=no-member
# -*- encoding: utf-8 -*-
'''
@File    :   斗地主.py
@Time    :   2019/10/05 16:50:12
@Author  :   Kellan Fan 
@Version :   1.0
@Contact :   kellanfan1989@gmail.com
@Desc    :   None
'''

# here put the import lib

class Poker(object):
    def __init__(self):
        self.one_row = [2,1,'K','Q','J',10,9,8,7,6,5,4,3]
        self.all = self.one_row*4

if __name__ == '__main__':
    p = Poker()
    print(p.all)