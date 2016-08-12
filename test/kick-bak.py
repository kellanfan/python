#!/usr/bin/python
from random import choice
score_you=0
score_he=0
direction=['right','centor','left']


def compare(num1,num2):
    if num1 < num2:
        print "you lose!!"
        return False;
    elif num1 > num2:
        print "you win!!!"
    else:
        print "draw!!!"


for i in range(5):
    print '===Round %d - You kick!===' %(i+1)
    print ("please choice which onside you shot: ")
    print 'right,centor,left'
    you=raw_input()
    print 'you kicked ' + you
    he=choice(direction)
    if you in direction:
        if you != he:
            print 'gold!!!'
            score_you +=1
        else:
            print 'oh!no!!!'
    else:
        print "please input 'right','centor','left'"
    print "Now the score is %d:%d" %(score_you,score_he)

    print '===Round %d - You save!===' %(i+1)
    print ("please choice which onside you save: ")
    print 'right,centor,left'
    you=raw_input()
    print 'you saved ' + you
    he=choice(direction)
    if you in direction:
        if you != he:
            print 'oh!no!!!'
            score_he +=1
        else:
            print 'yes!!!'
    else:
        print "please input 'right','centor','left'"
    print "Now the score is %d:%d" %(score_you,score_he)
compare(score_you,score_he)
