#!/usr/bin/env python3
# -*- coding:utf-8 -*-


import time
import threading

blance = 0
lock = threading.Lock()


def change_it(n):
    global blance
    blance += n


def run_thread(n):
    lock.acquire()
    try:
        change_it(n)
    finally:
        lock.release()


