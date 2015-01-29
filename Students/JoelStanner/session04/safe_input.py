#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
Improving raw_input.
"""

def safe_input(prompt):
    try:
        user_input = raw_input(prompt)
        return user_input

    except (KeyboardInterrupt, EOFError):
        print("Try again.")
        return None
