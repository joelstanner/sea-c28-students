#!/usr/bin/env python
# -*- coding:  utf-8 -*-

# This module contants two timer context managers, one a class and another
#     a generator function style context managers using a decorator

import sys
import time
import codecs
from StringIO import StringIO
from contextlib import contextmanager


class Timer(object):
    """This is a timer context manager Class to time code execution.
    """
    def __init__(self, f=sys.stdout):
        self.f = f
        self.start_time = time.time()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        end_time = time.time() - self.start_time
        self.f.write(u"This code took {:f} seconds\n".format(end_time))
        return self


@contextmanager
def timer(f=sys.stdout):
    """This is a timer context manager to time code execution.
    """
    start_time = time.time()
    try:
        yield object()
    except Exception as e:
        print(u"A '%s' error occured." % e)
        raise e
    finally:
        end_time = time.time() - start_time
        f.write(u"This code took {:f} seconds\n".format(end_time))

if __name__ == "__main__":

    # This is a test to make sure that the context handler Class works
    with Timer() as t:
        for i in range(100000):
            i = i ** 20
    print(u"Done processing")


    # This is a test to make sure that the context handler Decorator works
    with timer() as t:
        for i in range(100000):
            i = i ** 20
    print(u"Done processing")

    # This is a test to make sure that the context handler Class works
    f = StringIO()
    with Timer(f) as t:
        for i in range(100000):
            i = i ** 20
    print(u"Done processing")

    print(f.getvalue())
    f.close()

    # This is a test to make sure that the context handler Decorator works
    f2 = StringIO()
    with timer(f2) as t:
        for i in range(100000):
            i = i ** 20
    print(u"Done processing")

    print(f2.getvalue())
    f2.close()

    print(u"All tests succesful. First two are in different order than")
    print(u"last two because the timer is writing to the default sys.stdout")
    print(u"so timer output comes out on the screen right away.")
    print(u"\nThis last test makes sure exceptions handler works:")
    print(u"\n(only tests generator version)")

    # # This test make' sure that the exception in the context handler works
    with timer() as t:
        l = range(500)
        i = 0
        while True:
            i += 1
            l[i] = 1
        print(u"How long does this time take")


       
