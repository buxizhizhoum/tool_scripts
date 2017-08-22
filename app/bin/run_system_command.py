#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
how python run the system command
"""
# using command
import commands
batcmd = "dir"
result = commands.getoutput(batcmd)
print result


# using os.system() will print the result directly
import os
os.system("ls")


# using os.popen() to get an object, which is useful when process file.

# using tail of linux to get last line of a file
last_line = os.popen("tail -n 1 %s" % "../tmp/log_test.log").read()
print last_line
