#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
some function used to process timestamp and datetime

time.time() get the timestamp

time.localtime() convert timestamp to time struct, a format near to datetime
time.mktime() convert time struct to timestamp

time.strftime() convert time struct  to str
time.strptime() convert str to time struct.
"""

import time
import datetime


def timestamp_to_datetime(timestamp, dt_format=None):
    """
    convert timestamp to datetime
    :param timestamp: timestamp
    :param dt_format: datetime format
    :return: datetime
    """
    dt_format = "%Y-%m-%d %H:%M:%S" if dt_format is None else dt_format

    time_struct = time.localtime(timestamp)
    dt_str = time.strftime(dt_format, time_struct)
    dt = datetime.datetime.strptime(dt_str, dt_format)
    return dt


def datetime_to_timestamp(dt, dt_format=None):
    """
    convert datetime to timestamp, if datetime is str, dt_format should be
    provided, otherwise dt_format could be None.
    :param dt: datetime in type of datetime or str in format of dt_format
    :param dt_format: datetime format
    :return: timestamp
    """
    if isinstance(dt, str):
        if dt_format:
            dt = datetime.datetime.strptime(dt, dt_format)
        else:
            raise ValueError("dt_fromat should not be None, when dt is str.")
    time_tuple = dt.timetuple()
    timestamp = time.mktime(time_tuple)

    return timestamp


def generate_15min_datetime(dt_format=None):
    """
    generate datetime with 15min interval

    eg. 2018-01-29 11:01:00 generate 2018-01-29 11:00:00, it is
    the start 15min point of a certain datetime
    :return: datetime
    """
    if dt_format is None:
        dt_format = "%Y%m%d_%H%M"
    current_dt_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # convert str to time struct
    t_struct = time.strptime(current_dt_str, "%Y-%m-%d %H:%M:%S")
    t_stamp = int(time.mktime(t_struct)) / (15 * 60) * (15 * 60)
    time_str = time.strftime(dt_format, time.localtime(t_stamp))
    # convert str to datetime
    res = datetime.datetime.strptime(time_str, dt_format)
    return res


if __name__ == "__main__":
    timestamp_test = time.time()
    print timestamp_to_datetime(timestamp_test)

    datetime_test = timestamp_to_datetime(timestamp_test)
    print datetime_to_timestamp(datetime_test)

    assert datetime_test == timestamp_to_datetime(timestamp_test)

    print generate_15min_datetime()
