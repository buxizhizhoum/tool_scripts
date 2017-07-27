This project is a summary of the tool scripts.

wrap_sql_columns.py:

    A script used to wrap columns of sql with "%()s" and produce insert sql
    which could be used in execute(sql, args) in pymysql or MySQLdb when args
    is dict or a sequence of dict if execute_many(sql, args) is used.

ticker_of_function.py
    
    This module contains a decorator which is used to calculate the execute 
    time of a function.

    When it is needed, just put @ticker before the definition of the function.

mysql_pool.py
    
    Create a mysql connection pool, which could be used in the following codes.

file_lock.py
    
    provide a method to lock a file, which could be used in multiprocesses.