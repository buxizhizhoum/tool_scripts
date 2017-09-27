#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
test whether args will be modified in function
"""
a = {i: i*i for i in range(10)}
b = 10
c = "hello world!"


def pop_list(x):
    for i in range(len(x)):
        x.pop(i)
    print x


def decrease(y):
    y = y-2
    print y


def slice(string):
    string = string[:2]
    print string


if __name__ == "__main__":
    print "-" * 10 + "original a" + "-" * 10
    print a
    print "-"*10 + "params in function" + "-"*10
    pop_list(a)
    print "-" * 10 + "a" + "-" * 10
    print a

    print "-" * 10 + "original b" + "-" * 10
    print b
    print "-" * 10 + "params in function" + "-" * 10
    decrease(b)
    print "-" * 10 + "b" + "-" * 10
    print b

    print "-" * 10 + " original c" + "-" * 10
    print c
    print "-" * 10 + "params in function" + "-" * 10
    slice(c)
    print "-" * 10 + "c" + "-" * 10
    print c
