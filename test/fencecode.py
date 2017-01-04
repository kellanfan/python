#!/usr/bin/python
import string

express = raw_input("what is your code?: ")
lenth = len(express)
print "you code lenth is %s" %lenth
def single_even(lenth):
    if lenth % 2 == 0:
        return lenth
    return lenth + 1
l = single_even(lenth)/2
list_code = []
i = 0
if lenth % 2 == 0:
    while i < l:
        list_code.append(express[i])
        list_code.append(express[i+l])
        i= i + 1
elif lenth % 2 == 1:
    l1 = (lenth - 1) / 2
    while i < l - 1:
        list_code.append(express[i])
        list_code.append(express[i+l])
        i= i + 1
    list_code.append(express[l1])
str_code = ''.join(list_code)
print str_code
