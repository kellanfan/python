#!/usr/bin/python
from random import randint
print "what num i think you guess?"
answer = randint(1,100)
guess = 0
time=0
f = open('game.txt')
score = f.read().split()
while guess != answer:	#bingo = False
			#while bingo == False:
    guess = input()
    time=time+1
    if answer < guess:
        print "too big"

    if answer > guess:
        print "too small"
    if guess < 0:
        print "Exit..."
        break
if answer == guess:
    print "the num is %d and you guess time is %d" %(answer,time)
