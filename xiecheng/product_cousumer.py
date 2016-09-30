#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# created by liaozq 2016/09/30

# 生产者消费者协程demo


def consumer():
	r = ''
	while True:
		n = yield r
		if not n:
			return
		print('[consumer] consumering %s ' % n)
		r = '200 ok'


def produce(c):
	c.send(None)
	n = 0
	while n<5:
		n=n+1
		print('[producer] producing %s' % n)
		r = c.send(n)
		print('[producer] consumer return %s' % r)
	c.close()


if __name__ == '__main__':
	c = consumer()
	produce(c)
