#!/usr/bin/env python3
# -*- coding:utf-8 -*-


l = ['mickael', 'a', 'c']
print(l)
print(l[0:2])
print(l[-1])
m = list(range(100))
print(m)
# 取前10个
print(m[:10])
# 取最后10个
print(m[-10:])
# 从前10个中，每2个取一个
print(m[:10:2])

# 20-30 每2个取一个
print(m[20:30:2])

# 复制整个
print(m[:])