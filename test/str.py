#!/usr/bin/python
# -*- coding: UTF-8 -*-
import string
str = "this is string example....wow!!!"
print "The str is :" + str
print "str.center(30, 'a'): ", str.center(30, 'a')

sub = "i";
print "str.count(sub, 4, 40) : ", str.count(sub, 4, 40)
sub = "wow";
print "str.count(sub) : ", str.count(sub)

suffix = "wow!!!";
print str.endswith(suffix);
print str.endswith(suffix,20);

suffix = "is";
print str.endswith(suffix, 2, 4);
print str.endswith(suffix, 2, 6);

str1 = "this is\tstring example....wow!!!";

#tab 符号('\t')默认的空格数是 8
print "Original string: " + str1;
print "Defualt exapanded tab: " +  str1.expandtabs();
print "Double exapanded tab: " +  str1.expandtabs(16);

str2 = "exam";

print str.find(str2);
print str.find(str2, 10);
print str.find(str2, 40);

print str.upper()
print str.lower()
print str.title()
print str.swapcase()
