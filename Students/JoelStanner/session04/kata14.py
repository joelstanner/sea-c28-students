#!/usr/bin/python
# -*- coding: UTF-8 -*-


"""
Coding Kata 14 - Dave Thomas

http://codekata.com/kata/kata14-tom-swift-under-the-milkwood/

Use The Adventures of Sherlock Holmes as input:

http://codefellows.github.io/sea-c28-students/_downloads/sherlock.txt

Experiment with different lengths for the lookup key. (3 words, 4 words,
3 letters, etc)
"""


txt_file = u"sherlock_tester.txt"


def readfile(txt_file):
    """Read the text file, make a giant string"""

    with open(txt_file, 'r') as in_file:
        all_words = []
        for line in in_file:
            all_words.append(line)

    return u" ".join(all_words)


def collect_words(text):
    """Strip punctuation from a string."""

    punc = ur'!"#$%&\()*+,./:;<=>?@[\\]^_`{|}~'

    text = text.lower()
    text = text.strip(punc)
    words = text.split()

    return words


def trigram(words):
    """Make a trigram dict from the words"""

    word_pairs = {}

    for word in enumerate(words[:-2]):
        pair = tuple(words[word[0]:word[0]+2])
        follower = words[word[0]+2]
        word_pairs.setdefault(pair, []).append(follower)

    return word_pairs


