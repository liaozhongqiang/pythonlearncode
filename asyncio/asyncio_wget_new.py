#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import asyncio


async def wget(host):
	print('wget host %s start' % host)
	connect = asyncio.open_connection(host,80)
	reader,writer = await connect
	header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
	writer.write(header.encode('utf-8'))
	await writer.drain()
	while True:
		line = await reader.readline()
		if line == b'\r\n':
			break;
		print("host %s header >>>> %s" % (host,line.decode('utf-8')))
	writer.close()


if __name__ == '__main__':
	loop = asyncio.get_event_loop()
	tasks = [wget(host) for host in ['www.sohu.com','www.sina.com.cn','www.163.com']]
	loop.run_until_complete(asyncio.wait(tasks))
	loop.close()