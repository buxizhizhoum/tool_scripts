#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
method used to trace exception
"""
import traceback

try:
    1/0
except ZeroDivisionError as e:
    print e
    # print "traceback", traceback.print_exc()
    tmp = traceback.format_exc()
    print "tmp:", tmp
    print "traceback", traceback.format_exc()

# import sys, traceback


# def run_user_code(envdir):
#     source = raw_input(">>> ")
#     try:
#         exec source in envdir
#     except:
#         print "Exception in user code:"
#         print '-'*60
#         traceback.print_exc(file=sys.stdout)
#         print '-'*60
#
# envdir = {}
# while 1:
#     run_user_code(envdir)

try:
    assert 1==2
except Exception as e:
    print "assert test"
