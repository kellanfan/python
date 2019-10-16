# pylint: disable=no-member
# -*- encoding: utf-8 -*-
'''
@File    :   斗地主.py
@Time    :   2019/10/05 16:50:12
@Author  :   Kellan Fan 
@Version :   1.0
@Contact :   kellanfan1989@gmail.com
@Desc    :   斗地主提示器
'''

# here put the import lib
import pandas as pd
class Poker(object):
    def __init__(self):
        init_dict = {}
        for i in range(1,11):
            init_dict[i] = 4
        init_dict['J'] = 4
        init_dict['Q'] = 4
        init_dict['K'] = 4
        init_dict['小王'] = 1
        init_dict['大王'] = 1
        self.plant = init_dict
    def show(self):
        data = pd.DataFrame.from_dict(self.plant,orient='index').T
        data.index = ['count']
        print(data)
        


if __name__ == '__main__':
    p = Poker()
    p.show()