#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
actor from python cookbook 3rd edition by David Beazley, Brian K. Jones
"""
import threading
import time
from Queue import Queue

QSIZE = 10


class ActorExit(Exception):
    pass


class Actor(object):
    def __init__(self, qsize=None):
        self._mailbox = Queue(qsize)

    def send(self, msg):
        self._mailbox.put(msg)

    def recv(self):
        msg = self._mailbox.get()
        if msg is ActorExit:
            raise ActorExit()
        return msg

    def close(self):
        self.send(ActorExit)

    def start(self):
        self._terminated = threading.Event()
        t = threading.Thread(target=self._bootstrap)

        t.daemon = True
        t.start()

    def run(self):
        while True:
            msg = self.recv()
            print(msg)

    def _bootstrap(self):
        try:
            self.run()
        except ActorExit:
            pass
        finally:
            self._terminated.set()

    def join(self):
        self._terminated.wait()


class PrintActor(Actor):
    def run(self):
        while True:
            msg = self.recv()
            time.sleep(1)
            print(msg)


if __name__ == "__main__":
    p = PrintActor(QSIZE)
    p.start()
    # p.send(1)
    # p.send(2)
    for i in range(10):
        p.send(i)
    print("send complete")
    p.close()
    p.join()
    print("end")
