#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
Using the dict constructor and zip, build a dictionary of numbers from zero to
fifteen and the hexadecimal equivalent (string is fine).
"""


d = dict(zip([x for x in xrange(16)], [hex(x) for x in (xrange(16))]))
print(d)