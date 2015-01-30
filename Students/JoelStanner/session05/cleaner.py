#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
Write a program that takes a filename and “cleans” the file be removing all the
leading and trailing whitespace from each line.

Read in the original file and write out a new one, either creating a new file
or overwriting the existing one.

Give your user the option of which to perform.

Use map() to do the work.

Write a second version using a comprehension.

sys.argv hold the command line arguments the user typed in. If the user types:

$ python the_script a_file_name
Then:

import sys
filename = sys.argv[1]
will get filename == "a_file_name"
"""

import sys
filename = sys.argv[1]
choice = ""
newfile = ""

def cleaner(filename, choice):
    """Take a filename and remove leading and trailing whitespace on each line"""
    with open(filename, "w") as f:
        for line in f:
            line = f.readlines()
            stripped_line = stripper(line)
            if choice == "n":
                pass


def option():
    while True:
        choice = raw_input("New file or overwrite existing[n/o]? ")
        if choice == "N" or "n":
            new_file_parts = filename.split('.',1)
            new_file_top = new_file_parts[0] + "_new."
            newfile = new_file_top + new_file_parts[1]
            return newfile
        elif choice == "O" or "o":
            return "o"
        else:
            choice = raw_input("Try again[n/o]? ")


def stripper(thing_to_strip):
    """Return a copy of a string with leading and trailing whitespace stripped"""
    return thing_to_strip.strip()
