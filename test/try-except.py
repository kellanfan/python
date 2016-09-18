#!/usr/bin/python

try:
    f = file('non-exist.txt')
    print "file opened"
    f.close()
except:
    print "not exist!!"
print "Done"
