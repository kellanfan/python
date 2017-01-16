#!/usr/bin/python
# -*- coding: UTF-8 -*-

import math

for num in range(10000):
    x = int(math.sqrt(num + 100))
    y = int(math.sqrt(num + 268))
    if ( x * x == num + 100) and (y * y == num + 268):
        print num
