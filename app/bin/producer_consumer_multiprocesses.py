#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Updated version, could pass name for producer and consumer and queue
when initializing
"""
import time
import random
from multiprocessing import Process
from multiprocessing import Queue  # Queue should from multiprocessing


class ProducerProcess(Process):
    """
    update, add name and queue when initializing.
    """
    def __init__(self, name, queue):
        super(ProducerProcess, self).__init__(name=name)
        self.queue = queue

    def run(self):
        nums = range(5)
        while True:
            num = random.choice(nums)
            # queue.put(num)  # this modify global variable.
            self.queue.put(num)
            print "%s Produced %s" % (self.name, num)
            time.sleep(random.random())


class ConsumerProcess(Process):
    """
    update, add name and queue when initializing.
    """
    def __init__(self, name, queue):
        super(ConsumerProcess, self).__init__()
        self.name = name  # different from producer name initializing
        self.queue = queue

    def run(self):
        while True:
            # both of the get method of below work
            # num = queue.get()  # this modify global variable
            num = self.queue.get()
            # queue.task_done()  # queue from multiprocess have no task_done()
            print "%s consumed %s" % (self.name, num)
            time.sleep(random.random())


if __name__ == "__main__":
    queue = Queue(10)

    producer_list = ["Tom", "Cat", "Dog"]
    consumer_list = ["Jerry", "Cow", "Chicken"]

    producers = [ProducerProcess(item, queue) for item in producer_list]
    consumers = [ConsumerProcess(item, queue) for item in consumer_list]

    # todo: when join() used, the threads could not run
    for producer in producers:
        producer.start()  # start each producer
        # producer.join()

    for consumer in consumers:
        consumer.start()  # start each consumer
        # consumer.join()
