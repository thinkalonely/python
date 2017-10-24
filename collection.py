# !/usr/bin/env python
# -*- utf-8 -*-

# namedtuple是一个函数，用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。
from collections import namedtuple
#  deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈
from collections import deque


# 定义坐标
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x, p.y)

# 定义 圆
Circle = namedtuple('Circle', ['x', 'y', 'r'])
circle = Circle(0, 0, 5)
print(circle.x, circle.y, circle.r)

q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)
