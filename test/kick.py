#!/usr/bin/python
from random import choice


#def compare(num1,num2):
#    if num1 < num2:
#        print "you lose!!"
#        return False;
#    elif num1 > num2:
#        print "you win!!!"
#    else:
#        print "draw!!!"
score = [0,0]
direction=['right','centor','left']
def kick():
    print '=== You kick!==='
    print ("please choice which onside you shot: ")
    print 'right,centor,left'
    you=raw_input()
    print 'you kicked ' + you
    he=choice(direction)
    if you in direction:
        if you != he:
            print 'gold!!!'
            score[0] += 1
        else:
            print 'oh!no!!!'
    else:
        print "please input 'right','centor','left'"

    print '===You save!==='
    print ("please choice which onside you save: ")
    print 'right,centor,left'
    you=raw_input()
    print 'you saved ' + you
    he=choice(direction)
    if you in direction:
        if you != he:
            print 'oh!no!!!'
            score[1] +=1
        else:
            print 'yes!!!'
    else:
        print "please input 'right','centor','left'"
    print "now the score is %d:%d"%(score[0],score[1])
for i in range(5):
    print '====Round %d===='%(i+1)
    kick()
if score[0] == score[1]:
    i=i+1
    print '====add time Round %d'%(i+1)
    kick()
if score[0] > score[1]:
    print 'you win!!!'
else:
    print 'you lose!!'
