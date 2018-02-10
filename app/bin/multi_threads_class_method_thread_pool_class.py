#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
multi thread with thread pool and function in class.
"""
import time
from concurrent.futures import ThreadPoolExecutor


def threaded(fn):
    def wrapper(*args, **kwargs):
        return thread_pool.submit(fn, *args, **kwargs)  # returns Future object
    return wrapper


class TryClass(object):
    """
    class to run mainly logic
    """
    time_to_sleep = 2

    @threaded
    def try_method(self):
        """
        method which will be run in a thread
        :return:
        """
        time.sleep(self.time_to_sleep)
        print("wake up")
    
    def try_multi_thread(self):
        for _ in range(100):
            # thread_pool is 10, so only 10 threads could be start
            # at a same time
            self.try_method()


if __name__ == "__main__":
    thread_pool = ThreadPoolExecutor(10)  # max 10 threads

    TryClass().try_multi_thread()

    thread_pool.shutdown()  # shutdown thread_pool
