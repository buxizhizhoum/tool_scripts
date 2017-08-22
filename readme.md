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

limit_execute_time.py

    A method used to limit execute time of a function which might has no 
    timeout parameter.

file_lock.py
    
    Provide a method to lock a file, which could be used in multiprocesses.
    
faster_os_walk.py
    
    This module introduce a faster module that could accelerate the traverse 
    directory.

logger.py
    
    A module encapsulated python logging, which make it easier to record log.

send_mail_linux.py

    A module used to send mail with the service of linux server without
    registering an mailbox.

send_mail_smtplib.py

    Send mail with smtplib, this need to supply the username and password of a
    mailbox

    When it is slow to send a mail with the service of linux, and it is not
    possible to change the host name of the machine to accelerate it, or there
    are other problems when sending mail with mail service on linux this method
    may be an alternative solution.