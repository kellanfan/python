# pylint: disable=no-member
# -*- encoding: utf-8 -*-
'''
@File    :   exec_bao.py
@Time    :   2019/06/04 15:33:08
@Author  :   Kellan Fan 
@Version :   1.0
@Contact :   kellanfan1989@gmail.com
@Desc    :   None
'''

# here put the import lib
 
# 导入 Phone 包
#import bao #这里是导入包，
#bao.Pots.Pots() #包名.模块名.函数名
#bao.Gcc.Gcc()

from bao import Pots #这样就是从包中导入了模块，其实就是多了一层包的概念
Pots.Pots()
