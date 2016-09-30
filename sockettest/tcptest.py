#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import socket

# 创建一个socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('218.17.227.194', 8687))
# header
_headerdata = 'POST http://218.17.227.194:8080/kow/qwopenacct.do?' \
              'TOKEN=e22511e671d4853b1295ae9860d01b53d4dfdee8adad7eec&' \
              'TOKEN_KEY=ecbb0ddd2c35727b958281fa4c951710&CHANNEL=17 ' \
              'HTTP/1.1\r\nContent-Type: {content_type}\r\nContent-Length: {content_length}\r\n' \
              'Host: 127.0.0.1\r\nConnection: close\r\n\r\n'
# body
bodydata = '{"SERVICE_ID":"10059"}'.encode('utf-8')
print(bodydata)
headerdata = _headerdata.format(content_type="application/json", content_length=len(bodydata))
print(headerdata)
# send
s.sendall(headerdata.encode('utf-8') + bodydata)
buffer = []
while True:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)
s.close()
# header, html = data.split(b'\r\n\r\n', 1)
# print(header.decode('utf-8'))
print(data.decode('utf-8'))
