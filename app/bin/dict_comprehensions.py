#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
dict comprehension

this module is used to change all of the values in a dict to None
"""
tmp = {"a": 1, "b": 2, "c": 3}

res = {k: None for k, v in tmp.items()}
print res
