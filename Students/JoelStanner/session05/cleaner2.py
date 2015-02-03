#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
same as cleaner.py, but this uses a list comprehension.
"""

import sys
filename = sys.argv[1]


def cleaner_listc(file_to_process):
    """Take a filename and remove leading and trailing whitespace on each
    line"""

    lines = []
    with open(filename, "r") as old_file:
        for line in old_file:
            lines.append(line)

    with open(file_to_process, "w") as f:
        cleaned_file = [stripper(line) for line in lines]
        text = '\n'.join(line for line in cleaned_file)
        text += '\n'  # end file with newline
        f.write(text)


def option():
    """Ask user for a choice. New file or overwrite file?"""

    print("New file will make a copy with '_new' in the filename.")
    while True:
        choice = raw_input("New file or overwrite existing[n/o]? ")
        if choice == "N" or choice == "n":
            # add '_new.' to filename, keep any remaining filename parts.
            new_file_parts = filename.split('.', 1)
            new_file_top = new_file_parts[0] + "_new."
            newfile = new_file_top + new_file_parts[1]
            return newfile
        elif choice == "O" or choice == "o":
            newfile = filename
            return newfile
        else:
            print("only 'n' or 'o' works here")


def stripper(thing_to_strip):
    """Return a copy of a string with leading and trailing whitespace
    stripped"""

    return thing_to_strip.strip()


if __name__ == '__main__':
    cleaner_listc(option())