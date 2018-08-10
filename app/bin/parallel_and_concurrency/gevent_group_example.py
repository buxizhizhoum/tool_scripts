#!/usr/bin/python
# -*- coding: utf-8 -*-
"""from: http://sdiehl.github.io/gevent-tutorial/#introduction, it is a
very good tutorial of gevent"""
import gevent
from gevent.pool import Group


def talk(msg):
    for i in xrange(3):
        print(msg)
        gevent.sleep(1)

g1 = gevent.spawn(talk, 'bar')
g2 = gevent.spawn(talk, 'foo')
g3 = gevent.spawn(talk, 'fizz')

group = Group()
group.add(g1)
group.add(g2)
group.join()

# compare with gevent_group.py below lines could be reached.
group.add(g3)
group.join()



