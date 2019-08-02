# pylint: disable=no-member
# -*- encoding: utf-8 -*-
'''
@File    :   01-从1加到指定数字.py
@Time    :   2019/08/02 16:48:05
@Author  :   Kellan Fan 
@Version :   1.0
@Contact :   kellanfan1989@gmail.com
@Desc    :   None
'''

# here put the import lib

import sys
def addto(num):
	s = 0
	for i in range(num):
		s = s + i
	return s

def main():
	try:
		num = input('what num you want add to: ')
		print("the sum is %s" %addto(num))
	except:
		print("please input number!")
		sys.exit()

if __name__ == '__main__':
	main()
