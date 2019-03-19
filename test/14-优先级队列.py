#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Mon 11 Mar 2019 03:43:29 PM CST

# File Name: 14-优先级队列.py
# Description:

"""

import heapq
class PriorityQueue(object):
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self,item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

q = PriorityQueue()
q.push('aa',1)
q.push('bb',5)
q.push('cc',2)
q.push('dd',1)
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())
