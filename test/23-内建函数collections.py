# pylint: disable=no-member
# -*- encoding: utf-8 -*-
'''
@File    :   23-内建函数collections.py
@Time    :   2019/05/13 10:21:45
@Author  :   Kellan Fan 
@Version :   1.0
@Contact :   kellanfan1989@gmail.com
@Desc    :   None
'''

# here put the import lib

#namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，
# 并可以用属性而不是索引来引用tuple的某个元素。很方便地定义一种数据类型，它具备tuple的不变性，
# 又可以根据属性来引用，使用十分方便.
from collections import namedtuple

Point = namedtuple('Point',['x', 'y'])
p = Point(1, 2)
print(p)
print(p.x)
print(p.y)

print("="*20)
#deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈
from collections import deque
import datetime

l = []
for i in range(100000):
    l.append(i)
begin = datetime.datetime.now()
l.append('ascdsacda')
end = datetime.datetime.now()
print("普通列表append耗时：{}".format(end-begin))
q = deque(l)
begin1 = datetime.datetime.now()
q.append('x')
end1 = datetime.datetime.now()
print("deque列表append耗时：{}".format(end1-begin1))
print("="*20)
#使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict
from collections import defaultdict
dd = defaultdict(lambda:'None')
dd['aa'] = 'cdsa'
print("存在的值：%s"%dd['aa'])
print("不存在的值：%s"%dd['nn'])
print("="*20)
#保持Key的顺序,注意，OrderedDict的Key会按照插入的顺序排列，不是Key本身排序
from collections import OrderedDict
d = dict([('b',2),('a',1),('c',3)])
print(d)
orderd = OrderedDict([('b',2),('a',1),('c',3)])
print(orderd)
print("="*20)
#Counter是一个简单的计数器，例如，统计字符出现的个数
from collections import Counter
c = Counter()
for i in 'ascsanclsaduhoqwncaskdncalsidosabckasndcbasdjojasndbciwefqoweihcac':
    c[i] = c[i] + 1
print(c)
