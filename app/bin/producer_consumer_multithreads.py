#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Updated version, could pass name for producer and consumer and queue
when initializing
"""
from threading import Thread
import time
import random
from Queue import Queue


class ProducerThread(Thread):
    """
    update, add name and queue when initializing.
    """
    def __init__(self, name, queue):
        super(ProducerThread, self).__init__(name=name)
        self.queue = queue

    def run(self):
        nums = range(5)
        while True:
            num = random.choice(nums)
            queue.put(num)
            print "%s Produced %s" % (self.name, num)
            time.sleep(random.random())


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
            time.sleep(random.random())


if __name__ == "__main__":
    queue = Queue(10)

    # simple method to start
    # producer = ProducerThread("Tom", queue)
    # consumer = ConsumerThread("Jerry", queue)
    # producer.start()
    # consumer.start()
    # producer.join()  # join block main process until all threads have finished
    # consumer.join()  # join is not necessary

    # another method to start
    producer_list = ["Tom", "Cat", "Dog"]
    consumer_list = ["Jerry", "Cow", "Chicken"]

    producers = [ProducerThread(item, queue) for item in producer_list]
    consumers = [ConsumerThread(item, queue) for item in consumer_list]

    # todo: when join() used, the threads could not run
    for producer in producers:
        producer.start()  # start each producer
        # producer.join()

    for consumer in consumers:
        consumer.start()  # start each consumer
        # consumer.join()
