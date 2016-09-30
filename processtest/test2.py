#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from multiprocessing import Pool
import os
import time
import random


def long_time_task(name):
    print('run task %s (%s)' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('task %s runs %0.2f senconds.' % (name, end - start))


if __name__ == '__main__':
    print('parent process %s ' % os.getpid())
    p = Pool(3)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('waiting all subprocess done')
    p.close()
    p.join()
    print('all process done')
