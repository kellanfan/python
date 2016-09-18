#!/usr/bin/python
score = {
    'tess':98,
    'king': 89,
    'kim': 79
}
print "king's score is %d" %score['king']

for name in score:
    print name

score['king']=90
del score['kim']
for name in score:
    print name,score[name]
