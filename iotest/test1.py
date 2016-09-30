#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from fun.fun1 import my_abs
import os

f = open('C:\\Users\\myzhong2012\\Desktop\\1.txt', 'r')
print(f.read())
f.close()

with open('C:\\Users\\myzhong2012\\Desktop\\1.txt', 'r') as f1:
    print(f1.readline())

# 指定编码格式 忽略错误
# with open('', 'r', encoding='gbk',errors='ignore') as f2:
#    print(f2.read())

with open('C:\\Users\\myzhong2012\\Desktop\\1.txt', 'w') as f3:
    f3.write("hello python")

print(my_abs(11))

print(os.sys.path)


