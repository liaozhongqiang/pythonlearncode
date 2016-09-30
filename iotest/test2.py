#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import pickle
import json

d = dict(a='1', b='2')
print(pickle.dumps(d))

with open('C:\\Users\\myzhong2012\\Desktop\\1.txt', 'wb') as f1:
    pickle.dump(pickle.dumps(d), f1)

with open('C:\\Users\\myzhong2012\\Desktop\\1.txt', 'rb') as f2:
    print(pickle.load(f2))

json1 = json.dumps(d)
print(json1)
d1 = json.loads(json1)
print(d1)
