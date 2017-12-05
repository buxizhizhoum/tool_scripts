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
    if type(datetime_time) == str:
        datetime_time = datetime.datetime.strptime(
            datetime_time, "%H:%M:%S").time()
    else:
        datetime_time = datetime_time.time()

    current_time = datetime.datetime.now().time()
    # calculate how long to sleep
    max_time = max(datetime_time, current_time)
    min_time = min(datetime_time, current_time)
    delta_hour = max_time.hour - min_time.hour
    delta_min = max_time.minute - min_time.minute
    delta_seconds = max_time.second - min_time.second

    total_seconds = delta_hour * 3600 + delta_min * 60 + delta_seconds
    print("sleeping %s seconds" % total_seconds)
    time.sleep(total_seconds)


if __name__ == "__main__":
    wake_time = "21:29:00"
    wake_at_certain_time(wake_time)
