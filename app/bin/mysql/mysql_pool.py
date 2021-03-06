#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
# download mysql-connector from mysql official site, and install.
# https://dev.mysql.com/doc/connector-python/en/connector-python-installation-binary.html
# pip install mysql-connector-python
import mysql.connector.pooling


dbconfig = {
    # "database": "test",
    # "user":     "joe",
    "host":"127.0.0.1",
    "port":"3306",
    "user":"root",
    "password":"123456",
    "database":"test",
}

# cnx = mysql.connector.pooling.MySQLConnectionPool(pool_name="mypool",
#                                                   pool_size=10,
#                                                   **dbconfig)
# conn = cnx.get_connection()
# cursor = conn.cursor()
# sql = "select * from store WHERE create_time < '2017-06-03'"
# cursor.execute(sql)
# res = cursor.fetchall()
# print res


class MySQLPool(object):
    """
    create a pool when connect mysql, which will decrease the time spent in 
    request connection, create connection and close connection.
    """
    def __init__(self, host="172.0.0.1", port="3306", user="root",
                 password="123456", database="test", pool_name="mypool",
                 pool_size=3):
        res = {}
        self._host = host
        self._port = port
        self._user = user
        self._password = password
        self._database = database

        res["host"] = self._host
        res["port"] = self._port
        res["user"] = self._user
        res["password"] = self._password
        res["database"] = self._database
        self.dbconfig = res
        self.pool = self.create_pool(pool_name=pool_name, pool_size=pool_size)

    def create_pool(self, pool_name="mypool", pool_size=3):
        """
        Create a connection pool, after created, the request of connecting 
        MySQL could get a connection from this pool instead of request to 
        create a connection.
        :param pool_name: the name of pool, default is "mypool"
        :param pool_size: the size of pool, default is 3
        :return: connection pool
        """
        pool = mysql.connector.pooling.MySQLConnectionPool(
            pool_name=pool_name,
            pool_size=pool_size,
            pool_reset_session=True,
            **self.dbconfig)
        return pool

    def close(self, conn, cursor):
        """
        A method used to close connection of mysql.
        :param conn: 
        :param cursor: 
        :return: 
        """
        cursor.close()
        conn.close()

    def execute(self, sql, args=None, commit=False):
        """
        Execute a sql, it could be with args and with out args. The usage is 
        similar with execute() function in module pymysql.
        :param sql: sql clause
        :param args: args need by sql clause
        :param commit: whether to commit
        :return: if commit, return None, else, return result
        """
        # get connection form connection pool instead of create one.
        conn = self.pool.get_connection()
        cursor = conn.cursor()
        if args:
            cursor.execute(sql, args)
        else:
            cursor.execute(sql)
        if commit is True:
            conn.commit()
            # TODO what is the difference between add_connection and close?
            # why when close is used, connection of mysql is not decrease, it
            # seems that it has the same effect with add_connection.
            # when add_connection is used it is faster than close
            # conn.close will finally use add_connection
            # self.pool.add_connection()
            # self.pool.add_connection(conn._cnx)
            # conn.close() # close conn seems enough.
            self.close(conn, cursor)
            return None
        else:
            res = cursor.fetchall()
            # self.pool.add_connection()
            # self.pool.add_connection(conn._cnx)
            # conn.close() # close conn seems enough.
            self.close(conn, cursor)
            return res

    def executemany(self, sql, args, commit=False):
        """
        Execute with many args. Similar with executemany() function in pymysql.
        args should be a sequence.
        :param sql: sql clause
        :param args: args
        :param commit: commit or not.
        :return: if commit, return None, else, return result
        """
        # get connection form connection pool instead of create one.
        conn = self.pool.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.executemany(sql, args)
        if commit is True:
            conn.commit()
            # self.pool.add_connection()
            self.close(conn, cursor)
            return None
        else:
            res = cursor.fetchall()
            # self.pool.add_connection()
            self.close(conn, cursor)
            return res


if __name__ == "__main__":
    mysql_pool = MySQLPool(**dbconfig)
    sql = "select * from store WHERE create_time < '2017-06-02'"

    # test...
    while True:
        t0 = time.time()
        for i in range(10):
            mysql_pool.execute(sql)
            print i
        print "time cousumed:", time.time() - t0

    # sql = "insert into elec_workshop_15min_2018(stat_time, " \
    #       "workshop_id, kwh, spfv, charge, p, pi, pe, kwhi, kwhe, " \
    #       "q, qi, qe, kvarhi, kvarhe) " \
    #       "values(%(stat_time)s, %(workshop_id)s, %(kwh)s, " \
    #       "%(spfv)s, %(charge)s, %(p)s, %(pi)s, %(pe)s, " \
    #       "%(kwhi)s, %(kwhe)s, " \
    #       "%(q)s, %(qi)s, %(qe)s, %(kvarhi)s, %(kvarhe)s) " \
    #       "on DUPLICATE KEY UPDATE stat_time = values(stat_time), " \
    #       "workshop_id = values(workshop_id), kwh = values(kwh), " \
    #       "spfv = values(spfv), charge = values(charge), " \
    #       "p = values(p), pi = values(pi), pe = values(pe), " \
    #       "kwhi = values(kwhi), kwhe = values(kwhe), q = values(q), " \
    #       "qi = values(qi), qe = values(qe), kvarhi = values(kvarhi), " \
    #       "kvarhe = values(kvarhe)"
    # self.mysql.execute_many_SQL_no_close(sql, data_dict, commit=commit)


