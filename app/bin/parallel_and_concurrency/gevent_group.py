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


def consumer(queue, name):
    while True:
        num = queue.get()
        gevent.sleep(1)
        print("consum {}: {}".format(name, num))


if __name__ == "__main__":
    q = Queue(10)
    single_producer = gevent.spawn(producer, q)
    # if these 3 lines are not commented, lines below is not reachable
    # producer_group = Group()
    # producer_group.add(single_producer)
    # producer_group.join()

    # start a batch of consumers firstly
    consumers = [gevent.spawn(consumer, q, i) for i in range(10)]
    new_consumer = gevent.spawn(consumer, q, "new")

    group = Group()
    [group.add(item) for item in consumers]

    # group.add(single_producer)
    # group.join() will join all spawned Greenlet no matter whether
    # they are added or not
    group.join()
    print("consumer group started")

    # todo: below lines are not reachable
    # add another consumer
    group.add(new_consumer)
    group.join()
    print("add a new consumer")
