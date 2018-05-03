#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
iter file line by line until there is an blank line or at the end of file
"""


def process_line(line):
    print(line)


if __name__ == "__main__":
    with open('mydata.txt') as fp:
        # second args of iter() is guard. if value yield from iter = '\n', stop
        for line in iter(fp.readline, '\n'):
            process_line(line)
