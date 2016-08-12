#!/usr/bin/python

def sayhello(someone):
    print 'hello!!!' + someone

sayhello('a')
sayhello('b')
sayhello('c')

def compare(num1,num2):
    if num1 < num2:
        print "too small!"
        return False;
    if num1 > num2:
        print "too big!"
        return False;
    if num1 == num2:
        print "bingo!!!"
        return True;
def compare1(num1,num2):
    if num1 < num2:
        print "too small!!"
    elif num1 > num2:
        print "too big!!!"
    else:
        print "bingno!!!"
