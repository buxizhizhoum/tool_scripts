#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
calculate datetime several months ago

ref: http://labix.org/python-dateutil
"""
import datetime
from dateutil.relativedelta import relativedelta


def months_ago(datetime_dt=None, months=None):
    """
    return datetime, several months ago
    :param datetime_dt:
    :param months:
    :return:
    """
    if datetime_dt is None:
        datetime_dt = datetime.datetime.now()
    if months is None:
        months = 0

    res = datetime_dt + relativedelta(months=months)
    return res


if __name__ == "__main__":
    print months_ago(months=-2)
