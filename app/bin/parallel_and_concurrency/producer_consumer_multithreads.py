#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Updated version, could pass name for producer and consumer and queue
when initializing
"""
import time
import random
from threading import Thread
from Queue import Queue

from itertools import chain


class ProducerThread(Thread):
    """
    update, add name and queue when initializing.
    """
    def __init__(self, name, queue):
        super(ProducerThread, self).__init__(name=name)
        self.queue = queue

    def run(self):
        nums = range(5)
        # while True:
        for i in nums:
            num = random.choice(nums)
            queue.put(num)
            print "%s Produced %s" % (self.name, num)
            time.sleep(1)


class ConsumerThread(Thread):
    """
    update, add name and queue when initializing.
    """
    def __init__(self, name, queue):
        super(ConsumerThread, self).__init__()
        self.name = name  # different from producer name initializing
        self.queue = queue

    def run(self):
        while True:
            num = queue.get()
            queue.task_done()
            print "%s consumed %s" % (self.name, num)
            time.sleep(1)


if __name__ == "__main__":
    queue = Queue(10)

    producer_list = ["Tom", "Cat", "Dog"]
    consumer_list = ["Jerry", "Cow", "Chicken"]

    producers = [ProducerThread(item, queue) for item in producer_list]
    consumers = [ConsumerThread(item, queue) for item in consumer_list]

    # when join() used, the threads could not run
    # because join will wait for the threads to end
    for producer in producers:
        # when main thread exit, daemon threads are killed automatically
        producer.daemon = True
        producer.start()  # start each producer
        # join() should not be placed here, otherwise, lines below
        # will be executed only after threads joined above have finished.
        # producer.join()

    for consumer in consumers:
        consumer.daemon = True
        consumer.start()  # start each consumer

    # if join is necessary
    # join should be placed after all threads have been started,
    for item in chain(producers, consumers):
        print item
        item.join()

print "started all threads"


