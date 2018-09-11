#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
spark application to test spark log, work with spark_logging.py
https://stackoverflow.com/questions/40806225/pyspark-logging-from-the-executor
"""
from pyspark.sql import SparkSession

spark = SparkSession \
    .builder \
    .appName("Test logging") \
    .getOrCreate()

try:
    spark.sparkContext.addPyFile('s3://YOUR_BUCKET/spark_logging.py')
except:
    # Probably running this locally. Make sure to have spark_logging in the PYTHONPATH
    pass
finally:
    import spark_logging as logging

def map_sth(s):
    log3 = logging.getLogger("executor")
    log3.info("Logging from executor")

    if log3.isEnabledFor(logging.DEBUG):
        log3.debug("This statement is only logged when DEBUG is configured.")

    return s

def main():
    log2 = logging.getLogger("driver")
    log2.info("Logging from within module function on driver")
    spark.range(100).rdd.map(map_sth).count()

if __name__ == "__main__":
    log1 = logging.getLogger("driver")
    log1.info("logging from module level")
    main()
