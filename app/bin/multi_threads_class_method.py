#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
from threading import Thread


class TryClass(object):
    # this var will be used in function which will be call by threads
    time_to_sleep = 1

    def _func_to_be_threaded(self):
        time.sleep(self.time_to_sleep)
        print("wake up")

    def func_to_be_threaded(self):
        for i in range(10):
            Thread(target=self._func_to_be_threaded).start()


if __name__ == "__main__":
    try_1 = TryClass()
    try_1.func_to_be_threaded()
