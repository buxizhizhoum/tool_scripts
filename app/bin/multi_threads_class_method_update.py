#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
after a method is decorated by decorator "make_multi_threads", the method will
run in a thread if it is called.

oppose that the requirement is to output 10 "wake up", two methods is
available:

    1. try_method:
        this method runs in a threads, and saves no time
    2. for loop plus try_method_simple, each loop will start a thread and will
        save more time, if it is not a cpu heavy task.
"""
import time
from threading import Thread


def make_multi_threads(fn):
    def thread_wrapper(*args, **kwargs):
        Thread(target=fn, args=args, kwargs=kwargs).start()
    return thread_wrapper


class TryClass(object):
    # this var will be used in function which will be call by threads
    time_to_sleep = 1

    @make_multi_threads
    def try_method(self):
        """
        this not work as multi threads, this method runs in a thread, if multi
        threads is needed, this method should be call multi times, each call
        will start a thread.
        :return:
        """
        for i in range(10):
            time.sleep(self.time_to_sleep)
            print("wake up")

    @make_multi_threads
    def try_method_simple(self):
        """
        better way to understand is to move for loop outside of the method, and
        each loop will start a thread.
        :return:
        """
        time.sleep(self.time_to_sleep)
        print("wake up")

    def multi_threads_try(self):
        """
        each loop will start a thread.
        :return:
        """
        for i in range(10):
            # each loop start a thread, and there will be 10 threads in total.
            self.try_method_simple()  # this part will run in a thread.


if __name__ == "__main__":
    try_1 = TryClass()
    handle = try_1.try_method()  # this only contain one thread

    # this will start 1 thread in each loop
    for i in range(10):
        try_1.try_method_simple()

    # this will start 1 thread in each loop.
    try_1.multi_threads_try()
