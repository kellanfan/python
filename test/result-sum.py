#!/usr/bin/python

f = open('result.txt')
lines = f.readlines()
f.close()
results= []
for line in lines:
    data = line.split()
    sum=0
    for score in data[1:]:
        sum += int(score)
    result= '%s\t:%d\n' %(data[0],sum)
    print result
    results.append(result)
scorces = open('scorces.txt','w')
scorces.writelines(results)
scorces.close()
