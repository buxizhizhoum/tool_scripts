#!/usr/bin/python
# -*- coding: utf-8 -*-
import datetime
import time


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
