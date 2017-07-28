#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
This module provide a method to limit the execute time of a function, this
might be useful when a function has the probability to hang up and without
a parameter to set timeout.

Before the function run, a signal is sent to the process, if the function 
could complete in certain time, the process could clear out the signal alarm, 
if not an alarm is triggered, which will cause the function to raise an 
Exception.

The below take request.post() as an example, request.post() has a parameter
that could set an timeout value, so it is not necessary to use this method, 
it is just an example.
"""
import requests
import time

import signal

url = "http://127.0.0.1:8000/acceptpost/"


# simple one

def signal_handler(signum, frame):
    raise Exception("Timed out!")


signal.signal(signal.SIGALRM, signal_handler)
signal.alarm(1)   # 1 seconds
try:
    req = requests.post(url=url, data={"a": 1})
    time.sleep(10)
except Exception, msg:
    print "Timed out!"
signal.alarm(0)
time.sleep(1)

"""--------------------------------------------------------------"""
"""
The with statement version of this is better because it eliminates the need 
to write the repetitive code of the try/finally construction. It’s easy to 
make your objects and functions capable of use in with statements by using 
the contextlib built-in module.
This module contains the contextmanager decorator, which lets a simple 
function be used in with statements. This is much easier than defining a new 
class with the special methods __enter__ and __exit__ (the standard way)
"""
# more graceful one

from contextlib import contextmanager


class TimeoutException(Exception):
    pass


@contextmanager
def time_limit(seconds):
    def signal_handler(signum, frame):
        raise TimeoutException, "Timed out!"
    signal.signal(signal.SIGALRM, signal_handler)
    signal.alarm(seconds)
    try:
        yield
    finally:
        signal.alarm(0)


while True:
    try:
        # limit the execution time of function
        with time_limit(1):
            requests.post(url, data={"a": 1}, timeout=1.1)
            # requests.post(url, data, verify=False)
        time.sleep(3)
    except TimeoutException, msg:
        print "Timed out!"
        # print msg
        raise TimeoutException, "Time out!"


