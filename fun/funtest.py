#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import math
from fun1 import my_abs


print(my_abs(10))

def power(x):
    return x * x


print(power(12))


def power(x, n):
    s = 1
    while n > 0:
        s = s * x
        n -= 1
    return s


print(power(5, 3))


def power(x, n=2):
    s = 1
    while n > 0:
        s = s * x
        n -= 1
    return s


print(power(5, 15))


def calc(*numbers):
    cals_sum = 0
    for n in numbers:
        cals_sum += n * n
    return cals_sum


sup = (1, 2, 3)
print(calc(*sup))


def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


person('张三', '20')
person('蛛丝', '30', city='北京')


def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


print(fact(1))

print(fact(5))

print(fact(10))


# 汉诺塔
def hanoi(n, a, b, c):
    if n == 1:
        print("move", a, c)
    else:
        hanoi(n - 1, a, c, b)
        print("move", a, c)
        hanoi(n - 1, b, a, c)


hanoi(3, "a", "b", "c")
