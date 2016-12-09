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
def cli(): 
    """command-line interface""" 
    arguments = docopt(__doc__) 
    print(arguments) 

if __name__ == '__main__': 
    cli()

