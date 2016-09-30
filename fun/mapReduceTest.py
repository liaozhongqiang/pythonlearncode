#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from functools import reduce


def f(x):
    return x * x


print(list(map(f, [1, 2, 3, 4, 5])))

print(list(map(str, [1, 2, 3, 4, 5])))


def add(x, y):
    return x + y


print(reduce(add, [1, 2, 3, 4]))

# 字符串转数字

print(list(x for x in '12345'))


def str2int(s):
    def fn(x, y):
        return x * 10 + y

    def char2num(ch):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[ch]

    return reduce(fn, map(char2num, s))


print(str2int('1234'))

l1 = ['adam', 'LISA', 'barT']


def normalize(name):
    return str.capitalize(name)


print(list(map(normalize, l1)))


def prod(x, y):
    return x * y


print(reduce(prod, [1, 2, 3]))


def str2float(s):
    def char2num(ch):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[ch]

    x, y = s.split('.')
    return reduce(lambda a, b: a * 10 + b, map(char2num, x)) + (
                                                               reduce(lambda d, e: d * 10 + e, map(char2num, y))) / pow(
        10, len(y))

print(str2float('12.1212'))
