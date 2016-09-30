#!/usr/bin/env python3
# -*- coding:utf-8 -*-


from datetime import datetime
from datetime import timedelta

now = datetime.now()
print(now)
print(type(now))

dt = datetime(2016, 5, 16, 12, 11, 12)
print(dt)

# 小数位表示毫秒值
print(dt.timestamp())

t = 1463371872.0
print(datetime.fromtimestamp(t))

# UTC时间
print(datetime.utcfromtimestamp(t))

# str 2 datetime

cday = datetime.strptime('2016-05-16 11:18:50', '%Y-%m-%d %H:%M:%S')
print(cday)

# datetime to str

print(now.strftime('%Y-%m-%d %H:%M:%S'))

# datetime加减

print(now + timedelta(hours=12))

print(now - timedelta(days=1))

print(now - timedelta(days=1, hours=1))
