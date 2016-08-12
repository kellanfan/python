#!/usr/bin/python
def Quadrant(x,y):
    if x>=0:
        if y >=0:
            print "1"
        else:
            print "2"
    else:
        if y >=0:
            print "3"
        else:
            print "4"

x=input('what first num you input:')
y=input('what senced num you input:')
Quadrant(x,y)
