#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
This scripts is used to add "()", "%" and "s" in sql, which will be used in
MySQLdb or pymysql, when execute sql with parameters. such as in the clauses 
below:

    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', 
                            passwd='', db='tkq1')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(sql, args)

the parameter sql in last clause should be something below if the 
parameter args is an dict or an sequence of dict if execute_many(sql, args) 
been used:

        "INSERT INTO one_minutes_data (store_name, address)
        VALUES (%(store_name)s, %(address)s)"
    
Generally, after we get the column we would like to insert values, such as 
"store_name" and "address", however we have to edit the parts after "VALUES"
manually, if there are too many columns, it would be boring and very easy
to make mistakes.

What wrap_columns does is to return a string that contains "%()s" in each 
words of the columns been provided.
for example, when "store_name, address" been provided, 
"(%(store_name)s, %(address)s)" will be returned.

Also a complete sql used to insert data is provided, it is made by 
function insert_sql_maker()
"""


class SQLprocessor(object):
    def __init__(self):
        pass

    def wrap_columns(self, columns):
        """
        Accept a string contains all of the columns, wrap it with "%()s" 
        and return
        :param columns: a string contains all of the columns, which you 
        would like to appear in sql eg: "store_name, address"
        :return: a string whose words has been wrap with "%()s", 
        eg: '%(store_name)s, %(address)s'
        """
        column_list = columns.split(",")
        # remove space, add %()s on each item of list
        tmp = ["%(" + item.strip(" ") + ")s" for item in column_list]
        # join the list to from a string
        result = ", ".join(tmp)
        return result

    def insert_sql_maker(self, table_name, columns):
        """
        Assemble insert sql based on table name and columns
        if table name is "store", columns is "store_name, address",
        sql would be: 
        
        INSERT INTO store (store_name, address) VALUES (%(store_name)s, %(address)s)
        
        :param table_name: table name to insert data
        :param columns:  columns to insert data
        :return:  insert sql
        """
        wrap_columns = self.wrap_columns(columns)
        sql = "INSERT INTO %s (%s) VALUES (%s)" \
              % (table_name, columns, wrap_columns)
        return sql


if __name__ == "__main__":
    test_string = "store_name, address"

    sql_processor = SQLprocessor()
    # wrap columns with "%()s"
    wrapped_columns = sql_processor.wrap_columns(test_string)
    # insert sql, a complete sql could be used in execute(sql, args) in pymysql
    insert_sql = sql_processor.insert_sql_maker(table_name="store",
                                                columns=test_string)
    print wrapped_columns
    print insert_sql
