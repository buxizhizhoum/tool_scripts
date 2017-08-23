#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Basic usage of producer and consumer, producer produce a random data to Queue
and consumer consume it from Queue.
"""
from threading import Thread
import time
import random
from Queue import Queue

queue = Queue(10)


class ProducerThread(Thread):
    def run(self):
        nums = range(5)
        global queue
        while True:
            num = random.choice(nums)
            queue.put(num)
            print "Produced", num
            time.sleep(random.random())


class ConsumerThread(Thread):
    def run(self):
        global queue
        while True:
            num = queue.get()
            # queue.task_done()
            print "Consumed", num
            time.sleep(random.random())


ProducerThread().start()
ProducerThread().start()
ConsumerThread().start()
