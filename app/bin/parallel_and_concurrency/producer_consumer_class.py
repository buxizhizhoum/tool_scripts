#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
the consumer and producer not inherit from Thread, the codes is less rely on
context of threading, and could be used at other places,
such as multiprocess.
"""
import random
import threading
import time
from Queue import Queue


class Producer(object):
    def __init__(self, queue):
        self.queue = queue

    def run(self, n):
        nums = range(n)
        while True:
            number = random.choice(nums)
            self.queue.put(number)
            print("produce {}".format(number))
            time.sleep(0.1)


class Consumer(object):
    def __init__(self, queue):
        self.queue = queue

    def run(self):
        while True:
            res = self.queue.get()
            print("consume {}".format(res))
            time.sleep(1)


if __name__ == "__main__":
    q = Queue(10)
    producer = Producer(q)
    # consumer = Consumer(q)
    consumers = [Consumer(q) for i in range(10)]

    p = threading.Thread(target=producer.run, args=(10,))
    # c = threading.Thread(target=consumer.run)
    for consumer in consumers:
        c = threading.Thread(target=consumer.run)
        c.start()

    p.start()
    # c.start()

