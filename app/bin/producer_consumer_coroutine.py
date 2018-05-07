#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import time


def consumer():
    while True:
        x = yield
        print("received {}".format(x))
        time.sleep(1)
        print("consumed {}".format(x))



def producer(consu):
    next(consu)
    while True:
        product = random.randint(1, 10)
        print("produced {}".format(product))
        consu.send(product)
        time.sleep(1)
    consu.close()


if __name__ == "__main__":
    c = consumer()
    producer(c)


