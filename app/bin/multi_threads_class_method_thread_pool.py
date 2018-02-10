#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
multi threads with thread pool
"""
import time
from concurrent.futures import ThreadPoolExecutor


def threaded(fn):
    def wrapper(*args, **kwargs):
        return thread_pool.submit(fn, *args, **kwargs)  # returns Future object
    return wrapper


@threaded
def try_method():
    """
    function to run in a thread.
    :return:
    """
    time.sleep(1)
    print("wake up")


if __name__ == "__main__":
    thread_pool = ThreadPoolExecutor(10)  # max 10 threads

    for i in range(100):
        # thread_pool is 10, so only 10 threads could be start at a same time
        try_method()

    thread_pool.shutdown()  # shutdown thread_pool
