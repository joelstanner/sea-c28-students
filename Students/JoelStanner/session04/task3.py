#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
Using the dictionary from item 1: Make a dictionary using the same keys but 
with the number of ‘a’s in each value.
"""

d = {u'name': u'Chris', u'city': u'Seattle', u'cake': u'Chocolate'}

new_d = {}
for k, v in d.iteritems():
    new_d[k] = d[k].count('a')

print(new_d)
