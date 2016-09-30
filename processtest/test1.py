#!/usr/bin/env python3
# -*- coding:utf-8 -*-


from multiprocessing import Process
import os


# 子进程执行代码
def proc_run(name):
    print('Run child process %s (%s)' % (name, os.getpid()))


if __name__ == '__main__':
    print('Parent process %s.' % os.getppid())
    p = Process(target=proc_run, args=('test',))
    print('child process will start')
    p.start()
    p.join()
    print('child process run end')
