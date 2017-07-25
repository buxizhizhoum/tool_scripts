#!/usr/bin/python
# -*- coding: utf-8 -*-
import fcntl


full_name = "/tmp/test.txt"


def handle_file_with_lock(full_name):
    """
    a basic version
    :param full_name: filename to handle
    :return: 
    """
    fp = open(full_name, "w")
    try:
        # lock file， NB lock raise OSError if file is already locked
        fcntl.flock(fp.fileno(), fcntl.LOCK_EX)
        data = fp.read()
        fp.write("this is a string")
    except OSError as e:
        print e
    finally:
        fcntl.flock(fp, fcntl.LOCK_UN)
        fp.close()


def handle_file_with_lock_v1(full_name):
    """
    a more simple version
    :param full_name: filename to handle
    :return: 
    """
    with open(full_name, "w") as f:
        fcntl.flock(f.fileno(), fcntl.LOCK_EX)
        data = f.read()
        f.write("this is a string")
        fcntl.flock(f, fcntl.LOCK_UN)
