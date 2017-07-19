#!/usr/bin/python
# -*- coding: utf-8 -*-

test_dict = {"a": 10, "b": 1, "c": 3, "d": 6, "e": 5, "f": 9, "g": 2, "h": 7}
tmp = None

# res = {k: v for k, v in test_dict.iteritems()}
# print res
# print min(res)
print max([float(item) for item in test_dict.values()])
