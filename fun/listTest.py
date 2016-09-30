#!/usr/bin/env python3
# -*- coding:utf-8 -*-

d = list(range(1, 11))
print(d)

l = []
for x in range(1, 11):
    l.append(x * x)
print(l)

# 列表生成式
print([x * x for x in range(11)])

print([x * x * x for x in range(1, 2)])

print([x * x for x in range(1, 11) if x % 2 == 0])

print([d.lower() for d in ['Hello', 'World', 18, 'Apple', None] if isinstance(d, str)])


# 杨辉三角

# generator

def yanghui():
    n = [1]
    while True:
        yield n
        n.append(0)
        n = [n[i - 1] + n[i] for i in range(len(n))]


mi = 0
for m in yanghui():
    mi += 1
    if mi <= 6:
        print(m)
