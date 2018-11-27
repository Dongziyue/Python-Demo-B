#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time : 11/27/2018 16:16
# @Author : mingfei.net@gmail.com
# @FileName : collections_test.py
# @GitHub : https://github.com/thu/Python-Demo-B

from collections import namedtuple, deque, defaultdict, OrderedDict, Counter

# list tuple dict set

names = (1, 2, 3)

print(names[0])

# names[0] = 0

Point = namedtuple('Point', ['x', 'y'])

p = Point(1, 2)

print(p.x)
print(p.y)

print(isinstance(p, Point))
print(isinstance(p, tuple))

# p.x = 1

Circle = namedtuple('Circle', ['x', 'y', 'r'])

c = Circle(1, 2, 3)

print(c.x)
print(c.y)
print(c.r)

print(c._asdict())

# deque

names = [1, 2, 3]

names.append(4)

print(names)

print(names.pop())

print(names)

q = deque(names)

print(q)
print(q.pop())
print(q)

q.append(3)
print(q)

print(q.popleft())
print(q)

q.appendleft(1)
print(q)


def na():
    return 'N/A'  # not ava...


# d = defaultdict(na)

d = defaultdict(lambda: 'N/A')

d['key'] = 'value'

print(d)
print(d['key'])

print(d['k'])

# OrderedDict

d = dict([(1, 'x'), (2, 'y'), (3, 'z')])

print(d)

d = OrderedDict([(3, 'x'), (2, 'y'), (1, 'z')])

print(d)

# Counter

counter = Counter()

for c in 'programming':
    counter[c] += 1

print(counter)

words = ['hello', 'world', 'nice', 'world']
counter = defaultdict(lambda: 0)

for word in words:
    counter[word] += 1

print(counter)