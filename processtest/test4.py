#!/usr/bin/env python3
# -*- coding:utf-8 -*-


import time
import threading


def loop():
    print('thread %s is runing' % threading.current_thread().getName())
    n = 0
    while n < 5:
        n += 1
        print('thread %s >>> %s' % (threading.current_thread().getName(), n))
    print('thread %s end' % threading.current_thread().getName())


if __name__ == '__main__':
    print('thread %s is runing' % threading.current_thread().getName())
    t = threading.Thread(target=loop, name='LoopThread')
    t.start()
    t.join()
    print('thread %s end' % threading.current_thread().getName())
