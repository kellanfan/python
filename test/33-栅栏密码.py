# pylint: disable=no-member
# -*- encoding: utf-8 -*-
'''
@File    :   33-栅栏密码.py
@Time    :   2019/05/14 09:19:51
@Author  :   Kellan Fan 
@Version :   1.0
@Contact :   kellanfan1989@gmail.com
@Desc    :   栅栏密码，这里只分了2组。所谓栅栏密码，就是把要加密的明文分成N个一组，
             然后把每组的第1个字连起来，形成一段无规律的话。 不过栅栏密码本身有一个潜规则，
             就是组成栅栏的字母一般不会太多。
'''

# here put the import lib

import string

def single_even(lenth):
    if lenth % 2 == 0:
        return lenth
    return lenth + 1

def main():
    express = input("what is your code?: ")
    lenth = len(express)
    print("you code lenth is %s" %lenth)
    l = int(single_even(lenth)/2)
    list_code = []
    i = 0
    if lenth % 2 == 0:
        while i < l:
            list_code.append(express[i])
            list_code.append(express[i+l])
            i= i + 1
    elif lenth % 2 == 1:
        l1 = int((lenth - 1) / 2)
        while i < l - 1:
            list_code.append(express[i])
            list_code.append(express[i+l])
            i= i + 1
        list_code.append(express[l1])
    str_code = ''.join(list_code)
    print(str_code)

if __name__ == '__main__':
    main()
