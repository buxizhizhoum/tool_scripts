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
from concurrent.futures import Future
# if Future could not be imported, it could also be defined as below

# from threading import Event
# class Future(object):
#     def __init__(self):
#         self._ev = Event()
#
#     def set_result(self, result):
#         self._result = result
#         self._ev.set()
#
#     def set_exception(self, exc):
#         self._exc = exc
#         self._ev.set()
#
#     def result(self):
#         self._ev.wait()
#         if hasattr(self, '_exc'):
#             raise self._exc
#         return self._result


def call_with_future(fn, future, args, kwargs):
    try:
        result = fn(*args, **kwargs)
        future.set_result(result)
    except Exception as exc:
        future.set_exception(exc)


def make_multi_threads(fn):
    def thread_wrapper(*args, **kwargs):
        future = Future()
        thread = Thread(target=call_with_future, args=(fn, future, args, kwargs))
        thread.start()
        return future
    return thread_wrapper


class TryClass(object):
    # this var will be used in function which will be call by threads
    time_to_sleep = 1

    @make_multi_threads
    def try_method_simple(self):
        """
        better way to understand is to move for loop outside of the method, and
        each loop will start a thread.
        :return:
        """
        time.sleep(self.time_to_sleep)
        print("wake up")
        return "007"


if __name__ == "__main__":
    try_1 = TryClass()

    # this will start 1 thread in each loop
    for i in range(10):
        future_tmp = try_1.try_method_simple()
        res = future_tmp.result()  # will block until result is returned.
        print(res)
