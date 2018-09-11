#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
test script to log something in spark executor, work with spark_logger.py
https://stackoverflow.com/questions/40806225/pyspark-logging-from-the-executor
"""
import os
from pyspark import SparkContext
from pyspark import SparkConf


os.environ["PYSPARK_PYTHON"] = "/usr/bin/python3"
os.environ["PYSPARK_DRIVER_PYTHON"] = "/usr/bin/python3"
os.environ["LOG_DIRS"] = "/home/buxizhizhoum/2-Learning/spark_streaming/log/"
os.environ['PYSPARK_SUBMIT_ARGS'] \
    = '--packages org.apache.spark:spark-streaming-kafka-0-8_2.11:2.3.1 ' \
      'pyspark-shell'

conf = SparkConf().setAppName("log_test").setMaster("local[2]")
sc = SparkContext(conf=conf)

sc.addPyFile('/home/buxizhizhoum/2-Learning/spark_streaming/src/spark_logger.py')
import spark_logger
log = spark_logger.SparkLogger()


def map_sth(s):
    log.info("Mapping " + str(s))
    return s

sc.parallelize(range(10)).map(map_sth).count()


