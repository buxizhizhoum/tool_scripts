#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
wake up at certain time, this will be used when a script needs to run
at certain time of a day.

this version only support to wake up one time per day.
"""
import datetime
import time


def wake_at_certain_time(datetime_time):
    """
    wake up at certain time, time format hour:min:seconds

    "%H:%M:%S"

    :param datetime_time: time str in format of "%H:%M:%S"
    """
    current_time = datetime.datetime.now().strftime("%H:%M:%S:%f")

    # calculate how long to sleep
    delta_time = datetime.datetime.strptime(datetime_time, "%H:%M:%S") \
                 - datetime.datetime.strptime(current_time, "%H:%M:%S:%f")
    if delta_time.days < 0:
        delta_time = datetime.timedelta(days=0,
                                        seconds=delta_time.seconds,
                                        microseconds=delta_time.microseconds)

    total_seconds = delta_time.seconds + delta_time.microseconds / 1000.0
    print("sleeping %s seconds" % total_seconds)
    time.sleep(total_seconds)


if __name__ == "__main__":
    wake_time = "21:29:00"
    wake_at_certain_time(wake_time)
