#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
Create a dictionary containing “name”, “city”, and “cake” for “Chris” 
from “Seattle” who likes “Chocolate”.
"""

d = {u'name': u'Chris', u'city': u'Seattle', u'cake': u'Chocolate'}

print (d)

del d[u'cake']

print(d)

d[u'fruit'] = u'Mango'

print(d.keys())
print(d.values())

u'cake' in d

u'Mango' in d.values()
