#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
This module provide method to convert between timestamp and datetime
"""

import time
import datetime


timestamp = 1501459616


# method 1
def timestamp2datetime(timestamp):
    """
    change timestamp to datetime
    :param timestamp: timestamp to convert to datetime
    :return: datetime format data
    """
    datetime_data = datetime.datetime.fromtimestamp(timestamp)
    return datetime_data

print repr(timestamp2datetime(timestamp))


def datetime2timestamp(datetime_data):
    """
    convert datetime data to timestamp
    :param datetime_data: datetime data
    :return: timestamp
    """
    timestamp = time.mktime(datetime_data.timetuple())
    return timestamp

print repr(datetime2timestamp(datetime.datetime.now()))

