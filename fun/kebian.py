#!/usr/bin/env python3
# -*- coding:utf-8 -*-


def calc_sum(*args):
    asum = 0
    for n in args:
        asum += n
    return asum


print(calc_sum(1, 2, 3, 4, 5))


def lazy_sum(*args):
    def a_sum():
        ax = 0
        for n in args:
            ax += n
        return ax

    return a_sum


print(lazy_sum(1, 2, 3, 4, 5))

print(lazy_sum(1, 2, 3, 4, 5)())


def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    return fs


f1, f2, f3 = count()

print(f1())
print(f2())
print(f3())


def count2():
    return [lambda x=x: x * x for x in range(1, 4)]


print(count2())

f21, f22, f23 = count2()
print(f21())
print(f22())
print(f23())
