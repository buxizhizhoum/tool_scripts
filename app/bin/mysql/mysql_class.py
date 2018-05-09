#!/usr/bin/python
# -*- coding: utf-8 -*-
try:
    import MySQLdb
except ImportError:
    import pymysql as MySQLdb
import ConfigParser


class MySQLHandler(object):
    """
    处理数据库连接的class，需要配合Config文件使用
    """

    def __init__(self, cfg_path, db_name):
        """
        Avgs:
            cfg_path(str): config文件(.ini)的绝对路径
            db_name(str): 需要读取config文件中的数据库名字
        """
        self._cfg_path = cfg_path
        self._db_name = db_name
        self._conn = None
        self._cur = None

    def prompt_msg(self, msg):
        """
        输出本类各处的输出信息，调试时可以改为pass
        """
        pass
        # print msg

    def config_parser(self):
        """
        读取config文件的函数
        """
        conn_msg = {}
        try:
            config_handler = ConfigParser.ConfigParser()
            config_handler.read(self._cfg_path)
            # Set conn_msg.
            conn_msg['host'] = config_handler.get(self._db_name, 'host')
            conn_msg['port'] = config_handler.getint(self._db_name, 'port')
            conn_msg['database'] = config_handler.get(self._db_name,
                                                         'database')
            conn_msg['user'] = config_handler.get(self._db_name, 'username')
            conn_msg['passwd'] = config_handler.get(self._db_name, 'password')
        except Exception as e:
            raise e
        return conn_msg

    def connect_to_MySQL(self):
        """
        连接到数据库
        """
        conn_msg = self.config_parser()
        try:
            self._conn = MySQLdb.connect(
                host=conn_msg['host'],
                port=conn_msg['port'],
                user=conn_msg['user'],
                passwd=conn_msg['passwd'],
                db=conn_msg['database'],
                charset='utf8'
            )
            self._cur = self._conn.cursor(MySQLdb.cursors.DictCursor)
        except Exception as e:
            raise e

    @property
    def conn(self):
        """
        数据库连接的connection
        """
        if self._conn is None:
            self.connect_to_MySQL()
        return self._conn

    @property
    def cur(self):
        """
        数据库连接的cursor
        """
        if self._cur is None:
            self.connect_to_MySQL()
        return self._cur

    def close(self):
        """
        关闭数据库连接
        """
        try:
            self._cur.close()
            self._conn.close()
            self.prompt_msg('Close connection OK.')
        except Exception:
            self.prompt_msg('MySQL is not connected to be closed!')
        finally:
            self._cur = None
            self._conn = None

    def execute_SQL(self, sql, commit=False):
        """
        只执行一次查询，随即close connection
        """
        if self._conn is None and self._cur is None:
            self.connect_to_MySQL()
        # Main
        self._cur.execute(sql)
        if commit is True:  # UPDATE/INSERT/DELETE, no return.
            self._conn.commit()
            self.close()
            return None
        else:  # SELECT, has return.
            data = self._cur.fetchall()
            self.close()
            return data

    def execute_SQL_with_arg(self, sql, arg, commit=False):
        """
        只执行一次查询，随即close connection, 可以传入参数arg, 由pymsql自动拼接
        """
        if self._conn is None and self._cur is None:
            self.connect_to_MySQL()
        # Main
        self._cur.execute(sql, arg)
        if commit is True:  # UPDATE/INSERT/DELETE, no return.
            self._conn.commit()
            self.close()
            return None
        else:  # SELECT, has return.
            data = self._cur.fetchall()
            self.close()
            return data

    def execute_many_SQL(self, sql, args, commit=False):
        """
        执行多条sql
        """
        if self._conn is None and self._cur is None:
            self.connect_to_MySQL()
        # Main
        # self._cur.execute(sql)
        self._cur.executemany(sql, args)
        if commit is True:  # UPDATE/INSERT/DELETE, no return.
            self._conn.commit()
            self.close()
            return None
        else:  # SELECT, has return.
            data = self._cur.fetchall()
            self.close()
            return data

    def execute_SQL_no_close(self, sql, commit=False):
        """
        只执行一次查询，不关闭连接，需要在最后手动调用close()方法关闭
        """
        if self._conn is None and self._cur is None:
            self.connect_to_MySQL()
        # Main
        self._cur.execute(sql)
        if commit is True:  # UPDATE/INSERT/DELETE, no return.
            self._conn.commit()
            return None
        else:  # SELECT, has return.
            data = self._cur.fetchall()
            return data

    def execute_SQL_no_close_with_arg(self, sql, arg, commit=False):
        """
        只执行一次查询，随即close connection, 可以传入参数arg, 由pymsql自动拼接
        """
        if self._conn is None and self._cur is None:
            self.connect_to_MySQL()
        # Main
        self._cur.execute(sql, arg)
        if commit is True:  # UPDATE/INSERT/DELETE, no return.
            self._conn.commit()
            # self.close()
            return None
        else:  # SELECT, has return.
            data = self._cur.fetchall()
            # self.close()
            return data
