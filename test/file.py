#!/usr/bin/python
f = file('/root/python/test/data.txt')
data = f.read()
print data
f.close()
print "===="
g = file('/root/python/test/data.txt')
data1 = g.readline()
print data1
print "===="
h = file('/root/python/test/data.txt')
data2 = h.readlines()
print data2

