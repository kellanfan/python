#!/usr/bin/python
from random import randint
print "what num i think you guess?"
answer = randint(1,100)
guess = 0
time=0
while guess != answer:	#bingo = False
			#while bingo == False:
    guess = input()
    time=time+1
    if answer < guess:
        print "too big"

    if answer > guess:
        print "too small"
print "bingo,the num is %d" %answer
print "you guess time id %d" %time
print "the num is %d and you guess %d" %(answer,time)
