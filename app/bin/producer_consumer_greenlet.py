#!/usr/bin/python
# -*- coding: utf-8 -*-
import gevent
import random
import time
from gevent import Greenlet
from gevent import monkey
monkey.patch_all()
from gevent.queue import Queue  # coroutine safe queue of gevent


class Producer(Greenlet):
    def __init__(self, name, queue):
        Greenlet.__init__(self)
        self.name = name
        self.queue = queue

    def _run(self):
        """
        why the name start with _?
        in order to rewrite method of Greenlet
        :return:
        """
        while True:
            num = random.randint(1, 10)
            self.queue.put(num)
            print "Producer %s: produce %s" % (self.name, num)
            time.sleep(random.random())


class Consumer(Greenlet):
    def __init__(self, name, queue):
        Greenlet.__init__(self)
        self.name = name
        self.queue = queue

    def _run(self):
        while True:
            num = self.queue.get()
            print "Consumer %s: consume %s" % (self.name, num)
            time.sleep(random.random())


if __name__ == "__main__":
    q = Queue()
    t1 = Producer("task1", q)
    t2 = Producer("task2", q)
    t3 = Consumer("task3", q)

    t1.start()
    t2.start()
    t3.start()
    # here we are waiting all tasks
    gevent.joinall([t1, t2, t3])
