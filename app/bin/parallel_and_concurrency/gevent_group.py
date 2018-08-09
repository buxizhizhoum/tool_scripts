#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Group is used to manage a batch of async tasks."""

import random

import gevent
from gevent.pool import Group
from gevent.queue import Queue


def producer(queue):
    while True:
        num = random.randint(1, 10)
        queue.put(num)
        gevent.sleep(0.01)
        print("produce: {}".format(num))


def consumer(queue):
    while True:
        num = queue.get()
        gevent.sleep(1)
        print("consum: {}".format(num))


if __name__ == "__main__":
    q = Queue(10)
    single_producer = gevent.spawn(producer, q)
    # if these 3 lines are not commented, lines below is not reachable
    # producer_group = Group()
    # producer_group.add(single_producer)
    # producer_group.join()

    # start a batch of consumers firstly
    consumers = [gevent.spawn(consumer, q) for i in range(10)]

    group = Group()
    [group.add(item) for item in consumers]

    group.add(single_producer)
    group.join()
    print("consumer group started")

    # todo: below lines are not reachable
    # add another consumer
    new_consumer = gevent.spawn(consumer, q)
    group.add(new_consumer)
    group.join()
    print("add a new consumer")
