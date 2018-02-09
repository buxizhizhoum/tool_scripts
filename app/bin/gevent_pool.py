#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
gevent pool
"""
import time
from gevent.threadpool import ThreadPool


def my_func(text, num):
    while True:
        print text, num


pool = ThreadPool(100)
start = time.time()
for i in xrange(1000):
    pool.spawn(my_func, "Hello", i)

pool.join()
delay = time.time() - start
print('Take %.3f seconds' % delay)
