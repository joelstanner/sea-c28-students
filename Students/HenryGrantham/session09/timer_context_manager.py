#!/usr/bin/env python
# -*- coding:  utf-8 -*-
import sys
import time
from StringIO import StringIO
from contextlib import contextmanager


class Timer(object):
    """This is a timer contextmanager to time code execution.
    """
    def __init__(self):
        start_time = time.time()
        print '__init__()'
        self.start_time = time.time()

    def __enter__(self):
        print '__enter__()'
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        end_time = time.time() - self.start_time
        print(u"This code took {:f} seconds".format(end_time))

        print('__exit__')
        return self


@contextmanager
def timer():
    """This is a timer contextmanager to time code execution.
    """
    start_time = time.time()
    try:
        yield object()
    except Exception as e:
        print(u"A '%s' error occured." % e)
        raise e
    finally:
        end_time = time.time() - start_time
        print(u"This code took {:f} seconds".format(end_time))

@contextmanager
def print_encoded(encoding):
    old_stdout = sys.stdout
    sys.stdout = buff = StringIO()
    try:
        yield None
    finally:
        sys.stdout = old_stdout
        buff.seek(0)
        raw = buff.read()
        encoded = raw.encode(encoding)
        print encoded

if __name__ == "__main__":

    # This is a test to make sure that the context handler Class works
    with Timer() as foo:
        for i in range(100000):
            i = i ** 20
        print(u"How long does this time take")

    # This is a test to make sure that the context handler Decorator works
    with timer() as t:
        for i in range(100000):
            i = i ** 20
        print(u"How long does this time take")

    # This test make' sure that the exception in the context handler works
    with timer() as t:
        l = [1, 2, 3]
        i = 0
        while True:
            i += 1
            l[i] = 1
        print(u"How long does this time take")


       
