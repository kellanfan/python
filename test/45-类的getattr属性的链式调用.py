#/usr/bin/env python
# pylint: disable=no-member
# -*- encoding: utf-8 -*-
'''
@File    :   ex_chain.py
@Time    :   2019/06/04 14:54:20
@Author  :   Kellan Fan 
@Version :   1.0
@Contact :   kellanfan1989@gmail.com
@Desc    :   现在很多网站都搞REST API，像：http://api.server/user/timeline/list  
            如果要写SDK，给每个URL对应的API都写一个方法，那得累死，而且，API一旦改动，SDK也要改，
            利用完全动态的__getattr__，我们可以写出一个链式调用

'''

# here put the import lib

class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path
if __name__ == "__main__":
    print(Chain().status.user.timeline.list)