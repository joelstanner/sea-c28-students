#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
Create sets s2, s3 and s4 that contain numbers from zero through twenty, 
divisible 2, 3 and 4.
Display the sets.
Display if s3 is a subset of s2 (False)
and if s4 is a subset of s2 (True).
"""

s2 = set([x for x in xrange(21) if x % 2 == 0])
s3 = set([x for x in xrange(21) if x % 3 == 0])
s4 = set([x for x in xrange(21) if x % 4 == 0])

print s2
print s3 
print s4

print(s3.issubset(s2)) # False
print(s4.issubset(s2)) # True
