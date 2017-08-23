#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
When a pool is used, it seems that it is more proper to solve some problems
that Queue is not needed, which means the communication between process is
not necessary.

Pool is not suitable for producer and consumer
"""
import time
from multiprocessing import Process
from multiprocessing import Pool


class Math(Process):
    @staticmethod
    def square(num):
        res = num * num
        print "Produced %s" % res
        time.sleep(1)


def producer_fun(num):
    Math.square(num)


if __name__ == "__main__":
    p_math = Pool(10)
    p_consumer = Pool(10)

    for i in range(10):
        # p_math.apply(producer_fun, (i,))  # one process at a time
        p_math.apply_async(producer_fun, (i,))  # pool size process
    p_math.close()  # necessary before join()
    p_math.join()  # block to wait for all processes to end

    p_consumer.map(producer_fun, range(10))  # pool size process
