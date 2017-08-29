#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
producer and consumer with gevent

when python build in io processing is used, the monkey patch, which will patch
python standard library and makes it no block, has to been used, if not there
will be no effect of concurrency.

In this example, if time.sleep() or Queue of python is used, monkey patch
is necessary.
If gevent.sleep() is used, monkey patch is not necessary.
"""
import time
import gevent
from gevent import monkey
monkey.patch_all()
import random
from gevent.threadpool import ThreadPool
from gevent.queue import JoinableQueue
from gevent.queue import Empty
from gevent.queue import Queue
# from Queue import Queue


def consumer():
    """
    get something from queue
    """
    while True:
        item = q.get()
        print "consume", item
        # this works only when monkey patch is used.
        time.sleep(random.random())
        # this works no matter whether monkey patch is used.
        # gevent.sleep(random.random())


def producer():
    """
    put something to queue
    """
    while True:
        num = random.randint(1, 10)
        q.put(num)
        print "qsize is ___:", q.qsize()
        print "produce", num
        time.sleep(random.random())
        # gevent.sleep(random.random())


if __name__ == "__main__":
    q = Queue(10)

    # block start to start many producers and consumers
    producers = [gevent.spawn(producer) for i in xrange(20)]
    consumers = [gevent.spawn(consumer) for item in xrange(20)]
    gevent.joinall(producers)
    gevent.joinall(consumers)
    # block end to start many producers and consumers

    # block start to start one producer and one consumer
    # c = gevent.spawn(consumer)
    # p = gevent.spawn(producer)
    #
    # gevent.joinall([c, p])
    # block start to start one producer and one consumer
