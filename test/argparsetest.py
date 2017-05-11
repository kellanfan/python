#!/usr/bin/python

import argparse
import re, os, sys
Mes_Useage = '''%prog -l <filename>'''
parser = argparse.ArgumentParser(Mes_Useage)
parser.add_argument('-l', '--list', action = "store", dest = 'filename',help = 'use a long listing format')
parser.add_argument('-d', "--directory", action = "store", dest = "directory", help = "list directory entries instead of contents,and do not dereference symbolic links")
args = sys.argv[1:]
opt = args[0]
reg = r'-(.)'
or_data = re.compile(reg)
data = re.findall(or_data, opt)
(options, args) = parser.parse_args(args)
if data[0] == 'l':
    file = options.filename
    if os.path.isfile(file):
        cmd = "ls -l %s" %file
        os.system(cmd)
    else:
        print "Error: file %s is not exist!" %file
elif data[0] == 'd':
    dir = options.directory
    if os.path.isdir(dir):
        cmd = "ls -dl %s" %dir
        os.system(cmd)
    else:
        print "Error: directory %s is not exist!" % options.directory
else:
    print "Error"
