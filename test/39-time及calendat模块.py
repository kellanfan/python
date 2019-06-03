# pylint: disable=no-member
# -*- coding: UTF-8 -*-

import time
import calendar
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
print(time.strftime("%Y-%m-%d %H:%M:%S"))
cal = calendar.month(2017, 1)
print("以下输出2017年1月份的日历:")
print(cal)
