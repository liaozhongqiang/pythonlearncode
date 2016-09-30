#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from collections import Iterable

d = {'a': '11', 'b': '222'}
for key in d:
    print(key)

for ch in 'ABC':
    print(ch)

# 判断是否可以迭代

# True
print(isinstance('ABC', Iterable))

# True
print(isinstance(d, Iterable))

# True
print(isinstance([1, 2, 3], Iterable))

# False
print(isinstance(123,Iterable))


# 带下标迭代
for i, value in enumerate(['A', 'b', 'c']):
    print(i,value)

# 迭代两个变量
for x, y in [(1, 2), (3, 4)]:
    print(x, y)

# 迭代Map的Values
for value in d.values():
    print(value)

# 迭代Map的key,value
for key, value in d.items():
    print(key, value)