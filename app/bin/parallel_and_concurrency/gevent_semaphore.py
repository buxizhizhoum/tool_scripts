#!/usr/bin/python
# -*- coding: utf-8 -*-
from functools import partial

import gevent
from gevent.pool import Pool
from gevent.lock import BoundedSemaphore


def worker1(sem, n):
    """This is a better implementation, when Exception is raised, with clause
    will release semaphore finally"""
    with sem:
        gevent.sleep(1)
        print("worker1 processing {}".format(n))


def worker2(sem, n):
    """When Exception is raised, semaphore will not be released."""
    sem.acquire()
    gevent.sleep(1)
    print("work2 processing {}".format(n))
    sem.release()


if __name__ == "__main__":
    semaphore = BoundedSemaphore(9)
    pool = Pool()

    worker = partial(worker1, semaphore)
    pool.map(worker, range(10))

