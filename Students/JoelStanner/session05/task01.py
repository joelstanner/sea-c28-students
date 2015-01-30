feast = ['lambs', 'sloths', 'orangutans', 'breakfast cereals', 'fruit bats']
comprehension = [delicacy.capitalize() for delicacy in feast]

"""
What is the output of:

>>> comprehension[0]
???

>>> comprehension[2]
???
"""

# comprehension[0] == 'Lambs'
# comprehension[2] == 'Orangutans'
# -------------------------------------------------------------------------

feast = ['spam', 'sloths', 'orangutans', 'breakfast cereals', 'fruit bats']
comprehension = [delicacy for delicacy in feast if len(delicacy) > 6]

"""
What is the output of:

>>> len(feast)
???

>>> len(comprehension)
???
"""

# len(feast) == 5
# len(comprehension) == ['orangutans', 'breakfast cereals', 'fruit bats'] == 3
# ------------------------------------------------------------------------

list_of_tuples = [(1, 'lumberjack'), (2, 'inquisition'), (4, 'spam')]
comprehension = [ skit * number for number, skit in list_of_tuples ]

"""
What is the output of:

>>> comprehension[0]
???

>>> len(comprehension[2])
???
"""

# comprehension[0] == 'lumberjack'
# len(comprehension[2]) == 16
# -------------------------------------------------------------

list_of_eggs = ['poached egg', 'fried egg']
list_of_meats = ['lite spam', 'ham spam', 'fried spam']
comprehension = ['{0} and {1}'.format(egg, meat)
                     for egg in list_of_eggs
                     for meat in list_of_meats]

"""
What is the output of:

>>> len(comprehension)
???

>>> comprehension[0]
???
"""
# len(comprehension) == 2 ??? no 6... - got it.
# comprehension[0] == 'poached egg and light spam'
# ---------------------------------------------------------

comprehension = {x for x in 'aabbbcccc'}

"""
>>> comprehension
???
"""
# comprehension == {'a', 'b', 'c'}
# ----------------------------------------------

dict_of_weapons = {'first': 'fear',
                   'second': 'surprise',
                   'third': 'ruthless efficiency',
                   'forth': 'fanatical devotion',
                   'fifth': None}
dict_comprehension = (
    {k.upper(): weapon for k, weapon in dict_of_weapons.iteritems() if weapon}
)

"""
What is the output of:

>>> 'first' in dict_comprehension
???
>>> 'FIRST' in dict_comprehension
???
>>> len(dict_of_weapons)
???
>>> len(dict_comprehension)
???
"""

# 'first' == KeyError
# 'FIRST' == 'fear'
# len(dict_of_weapons) == 4 -- no... it's 5 -- oops was thinking dict_comp...
# len(dict_comprehension) == 4 -- oops wrong it's 5 too.
# -----------------------------------------------------------

"""
This is from CodingBat “count_evens” (http://codingbat.com/prob/p189616)

Using a list comprehension, return the number of even ints in the given array.

Note: the % “mod” operator computes the remainder, e.g. 5 % 2 is 1.

count_evens([2, 1, 2, 3, 4]) == 3
count_evens([2, 2, 0]) == 3
count_evens([1, 3, 5]) == 0
def count_evens(nums):
   one_line_comprehension_here
"""


def count_evens(nums):
    return len([num for num in nums if num % 2 == 0])
# ----------------------------------------------------


