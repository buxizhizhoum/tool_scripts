#!/usr/bin/python
# -*- coding: utf-8 -*-
"""from: http://sdiehl.github.io/gevent-tutorial/#actors

The main idea is that you have a collection of independent Actors which have
an inbox from which they receive messages from other Actors.
The main loop inside the Actor iterates through its messages and takes action
according to its desired behavior.
"""
import gevent
from gevent.queue import Queue


class Actor(gevent.Greenlet):
    def __init__(self):
        self.inbox = Queue()
        gevent.Greenlet.__init__(self)
        # super(self, Actor).__init__()

    def receive(self, msg):
        raise NotImplementedError

    def _run(self):
        self.running = True

        while self.running:
            msg = self.inbox.get()
            self.receive(msg)


class Pinger(Actor):
    def receive(self, msg):
        print msg
        pong.inbox.put("pong")
        gevent.sleep(1)


class Ponger(Actor):
    def receive(self, msg):
        print msg
        ping.inbox.put("ping")
        gevent.sleep(1)


ping = Pinger()
pong = Ponger()


if __name__ == "__main__":
    ping.start()
    pong.start()
    ping.inbox.put("start")
    gevent.joinall([ping, pong])

