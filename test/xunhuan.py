#!/usr/bin/env python3
#-*- coding: utf-8 -*-
from fun1 import my_abs


print(my_abs(10))

names=['a','b',11]
for name in names:
	print(name)

sum=0
for x in range(101):
	sum=sum+x

print("sum:",sum)

n=99
sum2=0
while n>0:
	sum2=sum2+n
	n=n-1

print("sum2:",sum2)