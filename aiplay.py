#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Fri 14 Dec 2018 09:48:40 AM CST

# File Name: aiplay.py
# Description:

"""
class Ai(object):
    def play(self):
        while True:
            ask = input("")
            #ask = unicode(ask, "utf-8")
            ask = ask.replace('?','!')
            ask = ask.replace(u'？','!')
            ask = ask.replace(u'吗','')
            print(ask)
            if ask == 'bye':
                break
            
ai = Ai()
ai.play()
