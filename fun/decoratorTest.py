#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import functools


def now():
    print("2016-05-15")


now()

print(now.__name__)


def log(func):
    def wrapper(*args, **kw):
        print("call %s():" % func.__name__)
        return func(*args, **kw)

    return wrapper


now2 = log(now)

print(now2.__name__)

now2()


@log
def now3():
    print(now3.__name__)


now3()


def log2(func):
    if callable(func):
        @functools.wraps(func)
        def wrapper1(*args, **kw):
            print('begin call %s()' % func.__name__)
            result = func(*args, **kw)
            print('end call %s()' % func.__name__)
            return result

        return wrapper1
    else:
        def decorator(truefunc):
            @functools.wraps(truefunc)
            def wrapper2(*args, **kw):
                print('begin call %s %s()' % (func, truefunc.__name__))
                result = truefunc(*args, **kw)
                print('end call %s %s()' % (func, truefunc.__name__))
                return result

            return wrapper2

        return decorator


@log2
def f111():
    return 1


print(f111())


@log2("execute")
def f112():
    return 2

f112()
