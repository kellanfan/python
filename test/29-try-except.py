# pylint: disable=no-member
# -*- encoding: utf-8 -*-
'''
@File    :   try-except.py
@Time    :   2019/05/13 16:24:53
@Author  :   Kellan Fan 
@Version :   1.0
@Contact :   kellanfan1989@gmail.com
@Desc    :   None
'''

# here put the import lib


try:
    f = file('non-exist.txt')
    print("file opened")
    f.close()
except:
    print("not exist!!")
print("Done")
