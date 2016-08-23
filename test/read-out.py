#!/usr/bin/python

data = file('data.txt')
out = open('out.txt','w')
#out = open('out.txt','a')
f = data.read()
out.write(f)
data.close()
out.close()
