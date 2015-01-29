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

def collect_words(text):
    """Strip punctuation from a string."""

    punc = ur'!"#$%&\()*+,./:;<=>?@[\\]^_`{|}~'

    text = text.lower()
    text = text.strip(punc)
    words = text.split()
    
    return words



def readfile(txt_file):
    with open(txt_file, 'r') as in_file:
        trigram = set()
        words = []
        for line in in_file:
            words = line.split()
            for word in enumerate(words):
                trigram.add(words[word[0]:word[0] + 3])
        print(trigram)
