#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from urllib import request
from urllib import parse
import json


'''
with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
    data = f.read()
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', data.decode('utf-8'))

req = request.Request('http://www.douban.com/')
req.add_header('User-Agent',
               'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) '
               'AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
with request.urlopen(req) as f1:
    data = f1.read()
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', data.decode('utf-8'))


form_data = parse.urlencode([('platform', 'web'), ('userId', '123'), ('question', '你好')])
req2 = request.Request('http://101.226.253.100:8000/robot/ask.action')
with request.urlopen(req2, data=form_data.encode('utf-8')) as f2:
    data = f2.read()
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', data.decode('utf-8'))

'''

# json

data_map = json.dumps(dict(SERVICE_ID='10059'))

req3 = request.Request('http://218.17.227.194:8687/kow/qwopenacct.do?TOKEN=e22511e671d4853b1295ae'
                       '9860d01b53d4dfdee8adad7eec&TOKEN_KEY=ecbb0ddd2c35727b958281fa4c951710&CHANNEL=17')

with request.urlopen(req3, data=data_map.encode('utf-8')) as f4:
    data = f4.read()
    print('Status:', f4.status, f4.reason)
    for k, v in f4.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', data.decode('utf-8'))
