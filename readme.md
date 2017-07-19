This project is a summary of the tool scripts.

wrap_sql_columns.py:

    A script used to wrap columns of sql with "%()s" and produce
    insert sql which could be used in execute(sql, args) in pymysql or MySQLdb
    when args is dict or a sequence of dict if execute_many(sql, args) is used.
