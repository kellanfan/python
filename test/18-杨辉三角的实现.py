# pylint: disable=no-member
# -*- encoding: utf-8 -*-
'''
@File    :   18-杨辉三角的实现.py
@Time    :   2019/05/06 13:09:54
@Author  :   Kellan Fan 
@Version :   1.0
@Contact :   kellanfan1989@gmail.com
@Desc    :   把杨辉三角的每一行作为list显示出来
'''

# here put the import lib

def triangles():
    tl = [1]
    while True:
        yield tl
        tl = [tl[i]+tl[i+1] for i in range(len(tl)-1)]
        tl.insert(0,1)
        tl.append(1)
        if len(tl) > 20:
            break

if __name__ == '__main__':
    for n in triangles():
        print(n)