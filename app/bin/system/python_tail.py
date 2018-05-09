#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
this is the version of python to implement "tail -f"
"""
import time


def monitor_file(filename, interval=None):
    """
    monitor the tail lines of a log file, is just like the linux command
    tail -f
    :param filename: filename to monitor
    :param interval: interval to refresh, default is 1 second
    :return:
    """
    with open(filename, "r") as f:
        f.seek(0, 2)  # move to the end of file
        while True:
            position = f.tell()  # get the position
            line = f.readline()

            sleep(interval)

            if line:
                yield repr(line)
            else:
                f.seek(position)
                print "no data"


def sleep(interval):
    """
    sleep some time according, this determines the refresh frequency
    :param interval:
    :return:
    """
    if interval is None:
        time.sleep(1)
    else:
        assert type(interval) in (int, float)  # ensure interval type
        time.sleep(interval)


if __name__ == "__main__":
    filename = "/app/log/test.log"  # log file to monitor
    for msg in monitor_file(filename):
        print msg
