#!/usr/bin/python

def name(word):
    l = len(word)
    n = 1
    s1 = ''
    f = word[0].upper()
    while n < l:
        s = word[n].lower()
        s1 = s1 + s
        n += 1
    return f + s1
youname = raw_input('what is your name: ')
print name(youname)
