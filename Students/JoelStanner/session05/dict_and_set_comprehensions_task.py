#!/usr/bin/python
# -*- coding: UTF-8 -*-

import copy

food_prefs = {u"name": u"Joel",
              u"city": u"Seattle",
              u"cake": u"Cheese",
              u"fruit": u"Lil' Cutie Orange",
              u"salad": u"Kale",
              u"pasta": u"Bow Tie"}

# 1
print(
    ('{name} is from {city}, and he likes {cake} cake, {fruit}s, '
     '{salad} salad, and {pasta} pasta.').format(**food_prefs)
)

# 2 - Using a list comprehension, build a dictionary of numbers from zero to
# fifteen and the hexadecimal equivalent (string is fine).

d = dict(zip([x for x in xrange(16)], [hex(x) for x in (xrange(16))]))
print(d)

# 3 - Do the previous entirely with a dict comprehension – should be a one-liner

d2 = {i: hex(i) for i in xrange(16)}
print(d2)

"""
4 Using the dictionary from item 1: Make a dictionary using the same keys
but with the number of ‘a’s in each value. You can do this either by editing
the dict in place, or making a new one. If you edit in place, make a copy first!
"""
food_prefs2 = copy.deepcopy(food_prefs)
food_prefs2 = {key: val.count(u'a') for key, val in food_prefs2.items()}
print(food_prefs2)


"""
Create sets s2, s3 and s4 that contain the numbers from zero through twenty
that are divisible 2, 3 and 4.
---Do this with one set comprehension for each set.
---What if you had a lot more than 3? – Don’t Repeat Yourself (DRY)
--------create a sequence that holds all three sets
--------loop through that sequence to build the sets up – so no repeated code.
Extra credit: do it all as a one-liner by nesting a set comprehension inside a
list comprehension. (OK, that may be getting carried away!)
"""

s2 = {x for x in xrange(21) if x % 2 == 0}
s3 = {x for x in xrange(21) if x % 3 == 0}
s4 = {x for x in xrange(21) if x % 4 == 0}

print(s2)
print(s3)
print(s4)

s2, s3, s4 = [{x for x in xrange(21) if x % y == 0} for y in xrange(2, 5)]

print(s2)
print(s3)
print(s4)
