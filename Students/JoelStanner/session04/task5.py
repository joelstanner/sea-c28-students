#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
Create a set with the letters in ‘Python’ and add ‘i’ to the set.
Create a frozenset with the letters in ‘marathon’
display the union and intersection of the two sets.
"""

s1 = {x for x in "Python"}
s1.add('i')

s2 = frozenset(x for x in 'marathon')

print(s1.union(s2))
print(s1.intersection(s2))