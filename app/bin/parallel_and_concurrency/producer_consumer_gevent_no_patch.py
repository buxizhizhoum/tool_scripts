#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
producer and consumer with gevent
no monkey patch is used.

I could not find where these codes from, if the author find this page, please
contact.
"""
import gevent
from gevent.queue import Queue, Empty


def worker(n):
    try:
        while True:
            task = tasks.get(timeout=1)
            print('Worker %s got task %s' % (n, task))
            gevent.sleep(0.1)
    except Empty:
        print('No task in queue!')


def boss():
    """
    Boss will wait to hand out work until a individual worker is
    free since the maxsize of the task queue is 3.
    """
    while True:
        for i in xrange(1, 10):
            tasks.put(i)
            gevent.sleep(0.1)
        print('Assigned all work!')


if __name__ == "__main__":
    tasks = Queue(maxsize=3)  # 限制队列的长度

    gevent.joinall([
        gevent.spawn(boss),
        gevent.spawn(worker, 'steve'),
        gevent.spawn(worker, 'john'),
        gevent.spawn(worker, 'bob'),
    ])
