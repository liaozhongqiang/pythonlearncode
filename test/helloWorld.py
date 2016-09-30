#!/usr/bin/env python3
#-*- coding: utf-8 -*-
print('hello world!')

# 中文测试

print('你好，python!')


# 字符串格式化

print('%.2f' % 3.1415926)

s1=72
s2=85
r=(85-72)*100/72
print(r)
print('%.1f%%' % r)
	
#list

mylist=['SB','DB','2逼']
print(mylist)
print('mylist的长度为%s' % len(mylist))
print('mylist的第一个元素为%s' % mylist[0])
print('mylist的最后一个元素为%s' % mylist[-1])

mylist.append('傻Ⅹ')

mylist.insert(1,'狗蛋')

mylist.pop()

mylist.pop(1)

print(mylist)

# tuple 其内的元素为不可变的

t=(1,2)

print(t)

print('tuple t 的第一个元素是%s' % t[0])

t=(1,2,['a',1])

print(t[0])

print(t[2][0])