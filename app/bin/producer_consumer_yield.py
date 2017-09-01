#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
the yield and next() could be used together to change code blocks when program
running

when there are something to be consume, the consumer will consume it.

how to do multi-producer and multi-consumer?
"""
import time
import sys
import random
from Queue import Queue


# producer
def produce(q):
    while True:
        i = random.randint(0, 9)
        q.put(i)
        print "produce", i
        yield i  # 'return' i, code below will not be execute this time
        time.sleep(1)


# consumer
def consume(q):
    p = produce(q)  # return generator, not execute
    while True:
        try:
            p.next()  # execute code from beginning to yield
            while q.qsize() > 0:
                print "consume", q.get()
        except StopIteration:
            sys.exit(0)


if __name__ == "__main__":
    q = Queue(10)
    consume(q)
