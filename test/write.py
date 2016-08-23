#!/usr/bin/python

data = 'I will be in a file.\nSo cool!'
out = open('output.txt','w')
out.write(data)
print out
out.close()
