#! /usr/bin/env python
"""
task 1 from Session03

I was attempting to make this python3 compatible, but we'll leave that alone for
now. It's just an excercize.
"""


fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']

print(fruits)

fruits.append(raw_input('fruit--->>>'))

print(fruits)

number = raw_input('number--->>>')

print('{0}: {1}'.format(number, fruits[int(number) - 1]))
