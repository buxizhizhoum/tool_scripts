#!/usr/bin/python
# -*- coding: utf-8 -*-
import datetime


class Cache(object):
    """
    class used to cache
    """
    _container = {}
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Cache, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self, expiration=None):
        """
        :param expiration: expiration seconds
        """
        # if no expiration is provided, set to inf
        self.expiration = expiration if expiration is not None else float("inf")

    @classmethod
    def cache(cls, k, v):
        """
        cache vaule
        :param k: key
        :param v: value
        :return:
        """
        cls._container[k] = v

    @classmethod
    def check(cls, k):
        """
        check the cached result
        :param k:
        :return:
        """
        res = cls._container.get(k)
        return res

    @classmethod
    def refresh(cls, k, v):
        cls._container[k] = v

    def expired(self, k):
        """
        check whether the cached data is expired
        :param k:
        :return:
        """
        dt_cached = self.check(k)
        if dt_cached is not None:
            dt_now = datetime.datetime.now()
            if (dt_now - dt_cached).total_seconds() >= self.expiration:
                return True
            else:
                return False
        # if not cached, return True
        else:
            return True


if __name__ == "__main__":
    cache = Cache()

    a = {i: i**2 for i in range(10)}
    for k, v in a.items():
        cache.cache(k, v)

    print "_"*60
    # test check
    for i in range(10):
        print cache.check(i)

    print "_"*60
    # test refresh
    for i in range(10):
        cache.refresh(i, i**3)

    for i in range(10):
        print cache.check(i)

