#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# if控制语句

a=True
if(a):
	print('你是好人！')

age=13
if(age>18):
	print('你是个成人了！')
elif(age<12):
	print('你还是个孩子！')
else:
	print('你是个少年了！')


height=1.75
weight=80.5
b=weight/(height*height)

if(b<18.5):
	print('过轻')
elif(18.5<= b<=25.0):
	print('正常')
elif(25<b<28.0):
	print('过重')
elif(28.0<b<32.0):
	print('肥胖')
else:
	print('严重肥胖')