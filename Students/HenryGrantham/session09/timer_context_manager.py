#!/usr/bin/env python
# -*- coding:  utf-8 -*-
import sys
import time
from StringIO import StringIO
from contextlib import contextmanager


class Context(object):
    """from Doug Hellmann, PyMOTW
    http://pymotw.com/2/contextlib/#module-contextlib
    """
    def __init__(self, handle_error):
        print '__init__(%s)' % handle_error
        self.handle_error = handle_error

    def __enter__(self):
        print '__enter__()'
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print '__exit__(%s, %s, %s)' % (exc_type, exc_val, exc_tb)
        return self.handle_error


@contextmanager
def timer():
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
    with timer():
        for i in range(100000):
            i = i ** 20
        print(u"How long does this time take")

    with timer():
        l = [1, 2, 3]
        i = 0
        while True:
            i += 1
            l[i] = 1
        print(u"How long does this time take")


       
