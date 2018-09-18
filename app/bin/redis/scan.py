#!/usr/bin/python
# -*- coding: utf-8 -*-
import redis


def keys(r, pattern, count=10000):

    original_cur = 0
    cur, first_scan_keys = r.scan(original_cur, match=pattern, count=count)

    res = first_scan_keys
    while cur != 0:
        cur, new_keys = r.scan(cur, match=pattern, count=count)
        if new_keys:
            res.extend(new_keys)

    return res


if __name__ == "__main__":
    print(keys(redis.Redis("127.0.0.1", 6379), pattern="*"))
