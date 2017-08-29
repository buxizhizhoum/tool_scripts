#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
timeout handle of gevent
"""
import gevent
from gevent import Timeout


def wait():
    gevent.sleep(2)


timer = Timeout(1).start()
thread1 = gevent.spawn(wait)  # 这种超时类型前面讲过

try:
    thread1.join(timeout=timer)
except Timeout:
    print('Thread 1 timed out')


timer = Timeout.start_new(1)  # start_new是一个快捷方式
thread2 = gevent.spawn(wait)


try:
    thread2.get(timeout=timer)  # get返回greenlet的结果,包含异常
except Timeout:
    print('Thread 2 timed out')

try:
    gevent.with_timeout(1, wait)  # 如果超时前返回异常,取消这个方法
except Timeout:
    print('Thread 3 timed out')


# from doc of genvet
timeout = Timeout(1)
timeout.start()
try:
    gevent.sleep(2)  # exception will be raised here, after *seconds* passed since start() call
finally:
    timeout.cancel()


# look here directly
"""
this method use signal to process timeout.
refer to the source code

Wrap a call to function with a timeout; if the called function fails to return 
before the timeout, cancel it and return a flag value, provided by 
timeout_value keyword argument.

If timeout expires but timeout_value is not provided, raise Timeout.

Keyword argument timeout_value is not passed to function.
"""
gevent.with_timeout(1, wait)  # most simply way to set timeout
