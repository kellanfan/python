# pylint: disable=no-member
# -*- encoding: utf-8 -*-
'''
@File    :   26-踢足球游戏.py
@Time    :   2019/05/13 12:02:17
@Author  :   Kellan Fan 
@Version :   1.0
@Contact :   kellanfan1989@gmail.com
@Desc    :   None
'''

# here put the import lib

from random import choice

def kick():
    direction = ['right','centor','left']
    print('=== Now, You kick!===')
    you=input("please choice which onside you shot, eg:<right,centor,left>: ")
    print('you kicked ' + you)
    he=choice(direction)
    if you in direction:
        if you != he:
            print('gold!!!')
            score[0] += 1
        else:
            print('oh!no!!!')
    else:
        print("please input 'right','centor','left'")
    print("now the score is %d:%d"%(score[0],score[1]))

    print('=== Now, You save!===')
    you=input("please choice which onside you save, eg:<right,centor,left>: ")
    print('you saved ' + you)
    he=choice(direction)
    if you in direction:
        if you != he:
            print('oh!no!!!')
            score[1] +=1
        else:
            print('yes!!!')
    else:
        print("please input 'right','centor','left'")
    print("now the score is %d:%d"%(score[0],score[1]))

if __name__ == '__main__':
    score = [0, 0]

    for i in range(5):
        print('====Round %d===='%(i+1))
        kick()
    while (score[0] == score[1]):
        i=i+1
        print('====add time Round %d'%(i+1))
        kick()
    if score[0] > score[1]:
        print('you win!!!')
    else:
        print('you lose!!')
