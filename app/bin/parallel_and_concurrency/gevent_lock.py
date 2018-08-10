#!/usr/bin/python
# -*- coding: utf-8 -*-
"""in fact, lock is unnecessary here, however when in multithreads,
it is necessary, because the switch of threads is not certain"""
import gevent
from gevent.lock import RLock


total = 0


def add(lock):
    global total
    for i in range(100000):
        with lock:
            total += 1
            gevent.sleep(0)


def subtract(lock):
    global total
    for i in range(100000):
        with lock:
            total -= 1
            gevent.sleep(0)


if __name__ == "__main__":
    l = RLock()
    add(l)
    subtract(l)
    print total

