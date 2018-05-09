#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
This module introduce a faster module that could accelerate the traverse 
directory.

scandir is a module that has the same api with os, and better performance 
than os especially when the directory tree is extremely large.

the address: https://github.com/benhoyt/scandir
"""
import timeit


import scandir
directory = "/media"
res = scandir.walk(directory)
for item in res:
    print item


# test os
import os


def with_os_walk():
    res = os.walk(directory)


print timeit.timeit(with_os_walk, number=10)

# test scandir


def with_scandir_walk():
    res = scandir.walk(directory)


print timeit.timeit(with_scandir_walk, number=10)

