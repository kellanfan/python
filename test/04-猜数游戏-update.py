#!/usr/bin/python

from random import ranint

#########open file#######
f = open('game.txt')
score = f.read().split()
game_times=score[0]
min_times=score[1]
totle_times=score[2]
print game_times
print min_times
print totle_times
if game_times > 0:
    avg_times = float(totle_times) / game_times
else:
    avg_times=0
print "you played %d times,the min time is %d,and the avg time is %2f" %(game_times,min_times,avg_times)
f.close()
########guess###############
num = ranint(1,100)
print "what is you name:"
name = raw_input()
print "what i think:"
bingo == False
times = 0
while bingo == False:
    time += 1
    answer = input()
    if answer > num:
        print "too big"
    if answer < num:
        print "too small"
    if answer == num:
        print "bingo!!!!"
        bingo == True

if game_times == 0 or min_times > times:
    min_times = times
total_times += times
game_times += 1
result = '%s %d %d %d'%(name,game_times,min_times,total_times)

############write file #############
f = file('game.txt','w')
lines = f.readlines()
scores = {}
for l in lines:
    s = l.split()
score = scores(name)
if score = None:
    score = [0,0,0]
scores[name]=[str(game_times),str(min_times),str(total_times)]
result = ''
for n in scores:
    line = n + ' ' + ' '.join(scores[n]) + '\n'
    result += line
f.write(result)
f.close()
