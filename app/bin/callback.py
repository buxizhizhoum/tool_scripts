#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
usage of callback
"""


def callback(*args):
    """
    the callback function
    :param args:
    :return:
    """
    print args
    for i in args:
        print i


def caller(args, callback):
    """
    call callback function
    :param args:
    :param callback:
    :return:
    """
    callback(args)


if __name__ == "__main__":
    for i in range(5):
        caller(i, callback)
