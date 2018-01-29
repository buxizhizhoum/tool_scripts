#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime
import time

INTERVAL = 15 * 60  # 15min


# def wake_at_certain_minute(wake_at):
#     tstruct = time.strptime(wake_at, "%Y-%m-%d %H:%M:%S")
#     tstamp = int(time.mktime(tstruct)) / (15 * 60) * (15 * 60)
#     time_str = time.strftime("%Y%m%d_%H%M", time.localtime(tstamp))
#
#     current_time = datetime.datetime.now().strftime("%M:%S:%f")
#
#     # calculate how long to sleep
#     delta_time = datetime.datetime.strptime(wake_at, "%M:%S") \
#                  - datetime.datetime.strptime(current_time, "%M:%S:%f")
#     if delta_time.days < 0:
#         delta_time = datetime.timedelta(days=0,
#                                         seconds=delta_time.seconds,
#                                         microseconds=delta_time.microseconds)
#
#     total_seconds = delta_time.seconds + delta_time.microseconds / 1000.0
#     print("sleeping %s seconds" % total_seconds)
#     time.sleep(total_seconds)

def how_about_sleep(shift=int(5),
                    interval=INTERVAL,
                    real_sleep=True):
    """
    sleep certain time, the base point is each 15min, shift could be used to
    decide the wake point.

    shift = 120 means 2 minutes later than the closest 15min.
    :param shift:
    :param interval:
    :param real_sleep:
    :return:
    """
    tmp = (int(time.time() - int(shift)) % interval)
    sleep_for_i = interval - tmp
    sleep_for = (sleep_for_i + abs(sleep_for_i)) / 2
    print('sleeping for %s' % (sleep_for))
    end_time_str = time.strftime('%Y-%m-%d %H:%M:%S',
                                 time.localtime(time.time() + sleep_for))
    print(end_time_str)
    if real_sleep:
        time.sleep(sleep_for)
    return sleep_for


if __name__ == "__main__":
    wake_time = "29:00"
    # wake_at_certain_minute(wake_time)
    while True:
        how_about_sleep(shift=-60)

