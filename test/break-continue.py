#!/usr/bin/python

i=0
for i in range(5):
    i += 1
    for j in range(3):
        if j ==1:
            break
        print "this j is %d" %j
    for h in range(3):
        if h ==1:
            continue
        print "the h is %d" %h
    print "the i is %d" %i
