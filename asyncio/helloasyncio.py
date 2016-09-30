#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio


@asyncio.coroutine
def hello():
	print('hello world !')
	# 异步调用sleep(1)
	r = yield from asyncio.sleep(1)
	print("hello again !")


if __name__ == '__main__':
	# 获取EventLoop
	loop = asyncio.get_event_loop()
	# 执行 coroutine
	loop.run_until_complete(hello())
	loop.close()