#!/usr/bin/python

word = 'helloword'
for c in word:
    print c
print '============'
print word[0]
print word[-2]
print word[5:7]
print word[:-5]
print word[:]
newworld = ','.join(word)
print newworld
