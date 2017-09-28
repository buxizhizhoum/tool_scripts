#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
provide a function that could sleep some time depends on the running time
of certain function.

t_start is the time before function runs
t_end is the time after function runs

INTERVAL is the interval expected between each running of the function.
"""
import time
import datetime


INTERVAL = 60 * 0.01


def main():
    time.sleep(1)


def sleep(interval):
    """
    sleep after the program run, ensure the interval between each running.
    :return:
    """
    if (t_end - t_start) < interval:
        print("sleeping")
        time.sleep(interval - (t_end - t_start))


if __name__ == "__main__":
    # the time before running something
    t_start = time.time()

    # do something here
    main()

    # the time after running something
    t_end = time.time()
    sleep(INTERVAL)
