#!/usr/bin/python

#coding: utf-8
"""Train tickets query via command-line.

Usage:
	tickets [-gdtkz] <from> <to> <date>

Options:
	-h,--help  help
	-g	gao tie
	-d	dong che
	-t	te kuai
	-k	kuai su
	-z	zhi da
Example:
    tickets beijing shanghai 2016-08-25
"""
from docopt import docopt
import sys
sys.path.append('../spider/misc')
import openurl
def cli(): 
    """command-line interface""" 
    arguments = docopt(__doc__) 
    print(arguments) 

if __name__ == '__main__': 
    url = 'https://kyfw.12306.cn/otn/leftTicket/queryA?leftTicketDTO.train_date=2018-10-16&leftTicketDTO.from_station=BJP&leftTicketDTO.to_station=CDW&purpose_codes=ADULT'
    ourl = openurl.OpenUrl(url)
    code , content = ourl.openurl()
    if code == 200:
        print(content)

