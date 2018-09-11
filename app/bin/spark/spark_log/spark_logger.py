#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
userd by spark_log to log something at executor
https://stackoverflow.com/questions/40806225/pyspark-logging-from-the-executor
"""
import os
import logging
import sys

from logging import handlers


class SparkLogger(object):
    basic_log_fmt = '%(asctime)s.%(msecs)03d %(levelname)s %(module)s ' \
                    '- %(funcName)s: %(message)s'
    rotating_log_fmt = '%(asctime)s - %(levelname)s ' \
                       '- %(name)s:%(lineno)s - %(message)s'

    @classmethod
    def setup_logger(cls):
        if 'LOG_DIRS' not in os.environ:
            sys.stderr.write('Missing LOG_DIRS environment variable, '
                             'pyspark logging disabled')
            return

        file = os.environ['LOG_DIRS'].split(',')[0] + '/pyspark.log'
        logging.basicConfig(filename=file, level=logging.INFO,
                            format=cls.basic_log_fmt)

    @classmethod
    def setup_rotating_log(cls):
        if 'LOG_DIRS' not in os.environ:
            sys.stderr.write('Missing LOG_DIRS environment variable, '
                             'pyspark logging disabled')
            return

        file_path = os.environ['LOG_DIRS'].split(',')[0] + '/pyspark_r.log'

        rotating_handler = logging.handlers.RotatingFileHandler(
            file_path, mode="a")
        fmt = logging.Formatter(cls.rotating_log_fmt)
        rotating_handler.setFormatter(fmt)
        logger = logging.getLogger("Spark_log")
        logger.setLevel("INFO")
        logger.addHandler(rotating_handler)

        logging.basicConfig(filename=file_path, level=logging.INFO,
                            format=cls.basic_log_fmt)

    def __getattr__(self, key):
        return getattr(logging, key)

# SparkLogger.setup_logger()
SparkLogger.setup_rotating_log()
