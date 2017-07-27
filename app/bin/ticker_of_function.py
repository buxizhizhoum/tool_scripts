#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
This module contains a decorator which is used to calculate the execute time
of a function.

Decorators have
the ability to run additional code before and after any calls to the 
functions they wrap. This allows them to access and modify input arguments 
and return values. This functionality can be useful for enforcing semantics, 
debugging, registering functions, and more

When it is needed, just put @ticker before the definition of the function.
"""
import time
import datetime


def ticker(func):
    # accept a function as parameter
    def print_info(*args, **kwargs):
        # do something before
        print "-- Started '%s' on %s " % (
            func.__name__,
            datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        )
        start_time = time.time()
        # run function
        result = func(*args, **kwargs)
        # do something after
        end_time = time.time()
        print "-- Finished '%s' on %s" % (
            func.__name__,
            datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        )
        print "Time consumed: %0.3f second(s)" % (end_time - start_time)
        return result

    print_info.__name__ = func.__name__
    # return the result of print_info which is result of func.
    return print_info


if __name__ == "__main__":
    @ticker
    def add(x, y):
        time.sleep(1)
        return x + y


    add(1, 2)
