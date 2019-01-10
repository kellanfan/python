#!/usr/bin/python
import sys
def addto(num):
	s = 0
	for i in range(num):
		s = s + i
	return s

def main():
	try:
		num = input('what num you want add to: ')
		print "the sum is %s" %addto(num)
	except:
		print "please input number!"
		sys.exit()

if __name__ == '__main__':
	main()
