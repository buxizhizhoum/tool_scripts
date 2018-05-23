#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
method 1
"""
# round down, if 1.0 < x <= 1.9, return 1 instead of 2
# round(x-0.5)
for x in [1.0, 1.3, 1.5, 1.7, 1.9]:
    print round(x - 0.5)

"""
method 2
"""
import math

x = 1.5666
# math.floor() return float in python2.7 and int in python3.6
y = math.floor(x * 10) / float(10)  # keep 1 digital, and round down
print y

"""
method 3, only round down to int
"""
# round down to int
x = 1.9999
y = x // 1
print y
