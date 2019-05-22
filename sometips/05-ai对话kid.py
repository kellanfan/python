# pylint: disable=no-member
# -*- encoding: utf-8 -*-
'''
@File    :   aiplay.py
@Time    :   2019/05/21 10:57:12
@Author  :   Kellan Fan 
@Version :   1.0
@Contact :   kellanfan1989@gmail.com
@Desc    :   None
'''

# here put the import lib

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
if __name__ == "__main__":
    ai = Ai()
    ai.play()
