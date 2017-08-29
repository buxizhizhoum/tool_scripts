#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
profile, used to analyse the time consuming of python
"""
import time


def foo():
    sum = 0
    for i in xrange(100):
        time.sleep(0.01)
    tmp = bar()
    return sum


def bar():
    sum = 0
    for i in range(10):
        time.sleep(0.05)
    return sum


if __name__ == "__main__":
    foo()

    # if run command in terminal, remove all the code below
    import cProfile

    # print result to terminal
    cProfile.run("foo()")
    # write result to file, ... need "pstats" to do analysis
    cProfile.run("foo()", "result")
    # another way is to use command line directly
    # >python -m cProfile test.py -o result
    # python -c "import pstats; p=pstats.Stats('result.out'); p.print_stats()"
    # python -c "import pstats; p=pstats.Stats('result.out'); p.sort_stats('time').print_stats()"

    import pstats

    # create Stats object
    p = pstats.Stats("result")
    # this line has the same effect with running cProfile.run("foo()")
    p.strip_dirs().sort_stats(-1).print_stats()
    # strip_dirs(): remove all dir information of all modules
    # sort_stats(): print info in module/name/line type
    # print_stats(): print all analysis info.

    # order by function name
    p.strip_dirs().sort_stats("name").print_stats()

    # order by running time
    # print_stats(3): print first 3 lines of all the info if parameter in int
    # print first % of info if parameter in float
    p.strip_dirs().sort_stats("cumulative").print_stats(3)

    # another method
    # p.sort_stats('time', 'cum').print_stats(.5, 'foo')
    # order by time, then order by cumulative, then print first 50% info.

    # if wish to know which function calls bar
    p.print_callers(0.5, "bar")

    # look for which function calls foo()
    p.print_callees("foo")
