#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
This module is used to parse command-line of python scripts.
"""

import argparse
import datetime
import sys


class CommandParser(object):
    def __init__(self):
        pass

    @classmethod
    def parse_command(cls):
        value = {}
        parser = argparse.ArgumentParser(description='args parse')
        parser.add_argument(
            "--dir",
            help="directory",
            default="/tmp")
        parser.add_argument("--filename", nargs="+", help="filenames")
        parser.add_argument("--time", help="time")
        args = parser.parse_args()
        value["filename"] = args.filename
        value["dir"] = args.dir
        value["time"] = cls.parse_datetime(args.time)
        cls.existance_judge(value)

        return value

    @classmethod
    def parse_datetime(cls, param):
        datetime_date = datetime.datetime.strptime(param,
                                                   "%Y/%m/%d/%H/%M/%S")
        return datetime_date

    @classmethod
    def existance_judge(cls, param_dict):
        if "dir" not in param_dict:
            print "'dir' is None! " \
                  "At least one of them is needed!\n--help to get help info."
            sys.exit(0)


if __name__ == "__main__":
    command_args = CommandParser.parse_command()
