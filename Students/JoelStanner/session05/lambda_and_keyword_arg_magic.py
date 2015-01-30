#!/usr/bin/python
# -*- coding: UTF-8 -*-


def fun_builder(n):
    """Return a list of n functions such that each one, when called, will return
    the input value, incremented by an increasing number."""

    fun_list = []
    for i in xrange(n):
        fun_list.append(lambda x, i=i: x + i)

    return fun_list

l = fun_builder(4)
print(l[0](2))  # --> 2
print(l[1](2))  # --> 3
