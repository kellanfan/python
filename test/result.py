#!/usr/bin/python

f = file('result.txt')
lines = f.readlines()
f.close()
scores=[]
for line in lines:
    data = line.split()
    print data
    sum = 0
    for score in data[1:]:
        sum += int(score)
    result = '%s\t%d\n' %(data[0],sum)
    scores.append(result)
g = file('scores.txt','w')
g.writelines(scores)
g.close()
