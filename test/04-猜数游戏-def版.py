#!/usr/bin/python

from random import randint
answer=randint(1,100)
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
        return False;
    elif num1 > num2:
        print "too big!!!"
        return False;
    else:
        print "bingno!!!"
        return True;
print "what num i think you guess"
bingo = False
while bingo == False:
    guess=input()
    bingo=compare1(guess,answer)
