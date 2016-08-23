#!/usr/bin/python

print "what you wate input:"
put = raw_input()
f = file('console.txt', 'w')
f.write(put)
f.close()
