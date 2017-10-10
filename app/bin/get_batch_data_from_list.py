#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
get more than one item from a list

this is firstly used to generate search condition when searching a batch
of data from database.
"""


def get_batch_from_list(items, scale=1):
    """
    get batch of data from a list each time instead of one by one,
    batch size is decided by scale.
    :param items: the list to get data from
    :param scale: the batch size
    :return:
    """
    for i in range(len(items)/scale + 1):
        if (i + 1) * scale < len(items):
            print(items[i*scale: i*scale + scale])
            return items[i*scale: i*scale + scale]
        else:
            if i*scale < len(items):
                print(items[i*scale: len(items)])
                return items[i*scale: len(items)]


if __name__ == "__main__":
    a = range(20)
    # how many data to get each time
    scale = 3
    get_batch_from_list(a, 3)
