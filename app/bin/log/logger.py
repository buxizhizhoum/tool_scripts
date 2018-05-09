#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
This module is used to encapsulate logging of python to a class, which
make it easier to instantiate an obj and record log.

The usage is easy, just get an instantiation of LogHandler and then get the 
logging obj by calling log_stream, log_file or log_rotating_file to get an 
logging obj to record log.
"""
import time

import logging
import os
from logging.handlers import RotatingFileHandler


class LogHandler(object):
    """
    this is the class that is used to produce logfile.
    """
    def __init__(self, log_dir, filename, level=None, format=None,
                 datefmt=None, mode="a"):
        """
        initialize basic config information of log
        :param log_dir: directory of log file
        :param filename: filename of log file
        :param level: log level, debug, info, warn, error, critical
        :param format: the format of log records
        :param datefmt: the format of date format, if date is needed in format
        :param mode: file mode
        """
        self.log_dir = log_dir
        self.filename = filename
        self.log_filename = os.path.join(self.log_dir, self.filename)
        self.level = logging.WARN if level is None else self.parse_level(level)
        format_log = '%(asctime)s %(filename)s line:%(lineno)d ' \
                     '%(levelname)s %(message)s'
        self.format = format_log if format is None else format
        self.datefmt = '%Y-%m-%d %H:%M:%S' if datefmt is None else datefmt
        self.mode = mode
        logging.basicConfig(
            level=self.level,
            format=self.format,
            datefmt=self.datefmt,
            filemode=self.mode)

    def parse_level(self, level):
        """
        parse log level from user input
        :param level: user input, string
        :return: log level in one of 5
        """
        level_tmp = level.upper()
        if level_tmp == "DEBUG":
            log_level = logging.DEBUG
        elif level_tmp == "INFO":
            log_level = logging.INFO
        elif level_tmp in ("WARN", "WARNING"):
            log_level = logging.WARN
        elif level_tmp == "ERROR":
            log_level = logging.ERROR
        elif level_tmp == "CRITICAL":
            log_level = logging.CRITICAL
        else:
            raise ValueError, "Wrong log level, please choose log level " \
                              "in 'debug', 'info', 'warn', 'error', " \
                              "'critical'."
        return log_level

    def log_stream(self):
        """
        stream output, useful to debug
        :return: logging obj
        """
        console = logging.StreamHandler()
        console.setLevel(self.level)
        formatter = logging.Formatter(self.format)
        console.setFormatter(formatter)
        res = logging.getLogger(self.log_filename)
        res.addHandler(console)
        return res

    def log_file(self):
        """
        log to a file, not control the file size
        :return: logging obj
        """
        # log_filename name, contain full path
        # if log_dir is not exist, make it.
        log_dir = os.path.split(self.log_filename)[0]
        if not os.path.isdir(log_dir):
            os.mkdir(log_dir)
        console = logging.FileHandler(self.log_filename)
        console.setLevel(self.level)
        formatter = logging.Formatter(self.format)
        console.setFormatter(formatter)
        res = logging.getLogger(self.log_filename)
        res.addHandler(console)
        return res

    def log_rotating_file(self, maxBytes=0, backupCount=0):
        """
        Open the specified file and use it as the stream for logging.

        By default, the file grows indefinitely. You can specify particular
        values of maxBytes and backupCount to allow the file to rollover at
        a predetermined size.

        Rollover occurs whenever the current log file is nearly maxBytes in
        length. If backupCount is >= 1, the system will successively create
        new files with the same pathname as the base file, but with extensions
        ".1", ".2" etc. appended to it. For example, with a backupCount of 5
        and a base file name of "app.log", you would get "app.log",
        "app.log.1", "app.log.2", ... through to "app.log.5". The file being
        written to is always "app.log" - when it gets filled up, it is closed
        and renamed to "app.log.1", and if files "app.log.1", "app.log.2" etc.
        exist, then they are renamed to "app.log.2", "app.log.3" etc.
        respectively.

        If maxBytes is zero, rollover never occurs.
        
        :return: logging obj
                """
        # if log_dir is not exist, make it.
        log_dir = os.path.split(self.log_filename)[0]
        if not os.path.isdir(log_dir):
            os.mkdir(log_dir)
        rt_handler = RotatingFileHandler(self.log_filename,
                                         mode=self.mode,
                                         maxBytes=maxBytes,
                                         backupCount=backupCount,
                                         encoding=None,
                                         delay=0)
        rt_handler.setLevel(self.level)
        formatter = logging.Formatter(self.format)
        rt_handler.setFormatter(formatter)
        res = logging.getLogger(self.log_filename)
        res.addHandler(rt_handler)
        return res


if __name__ == "__main__":
    log0 = LogHandler("/app/log", "test_1.log", level="DEBUG")
    log1 = LogHandler("/app/log/", "test1.log", level="INFO")
    log2 = LogHandler("/app/log/", "test.log", level="INFO")

    log_0 = log0.log_stream()
    log_1 = log1.log_file()
    log_2 = log2.log_rotating_file()

    log_0.debug("debug test...")
    log_1.error("log1test...")
    log_1.error("log1test...")
    log_2.info("log2info")
    log_2.error("log2test...")

    while True:
        log_2.error("log2test...")
        time.sleep(9)

