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


def cleaner_map(file_to_process):
    """Take a filename and remove leading and trailing whitespace on each line"""
    lines = []
    with open(filename, "r") as old_file:
        for line in old_file:
            lines.append(line)

    with open(file_to_process, "w") as f:
        cleaned_file = map(stripper, lines)
        text = '\n'.join(line for line in cleaned_file)
        text += '\n'  # end file with newline
        f.write(text)


def option():
    while True:
        print("New file will make a copy with '_new' in the filename.")
        choice = raw_input("New file or overwrite existing[n/o]? ")
        if choice == "N" or choice == "n":
            # add '_new.' to filename, keep any remaining filename parts.
            new_file_parts = filename.split('.',1)
            new_file_top = new_file_parts[0] + "_new."
            newfile = new_file_top + new_file_parts[1]
            return newfile
        elif choice == "O" or choice == "o":
            newfile = filename
            return newfile
        else:
            print("only 'n' or 'o' works here")


def stripper(thing_to_strip):
    """Return a copy of a string with leading and trailing whitespace stripped"""
    return thing_to_strip.strip()


if __name__ == '__main__':
    cleaner_map(option())

