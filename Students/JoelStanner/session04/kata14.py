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


import random
import string

TXT_FILE = u"sherlock.txt"


def readfile(txt_file):
    """Read the text file, make a giant string"""

    with open(txt_file, 'r') as in_file:
        all_words = []
        for line in in_file:
            all_words.append(line)

    return u" ".join(all_words)


def collect_words(text):
    """Strip punctuation from a string."""

    punc = unicode(string.punctuation)
    punc = string.punctuation.replace("'", "")  # keep apostropies
    punc = string.punctuation.replace("-", "")  # keep hyphenated words
    table = dict([(ord(c), None) for c in punc])

    text = text.lower()
    text = text.translate(table)
    words = text.split()

    # remove the bare single quotes
    # " ' " is both a quote and an apostrophe
    words = [word for word in words if word != "'"]

    return words


def trigram(words):
    """Make a trigram dict from the words"""

    word_pairs = {}

    for word in enumerate(words[:-2]):
        pair = tuple(words[word[0]:word[0]+2])
        follower = words[word[0]+2]
        word_pairs.setdefault(pair, []).append(follower)

    return word_pairs


def new_paragraph(word_pairs):
    """Make a new story from the trigrams"""

    new_story = []
    # random number of sentences in a paragraph
    for _ in range(random.randint(1, 10)):
        sentence = list(random.choice(word_pairs.keys()))

        # random number of words in a sentence
        for _ in range(random.randint(2, 20)):
            pair = tuple(sentence[-2:])
            # key error just ends the sentence:
            try:
                sentence.append(random.choice(word_pairs[pair]))
            except(KeyError):
                break
        # Capitalize the first word
        sentence[0] = sentence[0].capitalize()
        sentence[-1] += random.choice('?!.')
        new_story.extend(sentence)

    new_story = " ".join(new_story)

    return new_story

if __name__ == '__main__':

    trigrams_words = trigram(collect_words(readfile(TXT_FILE)))

    final_text = ""
    for _2 in range(random.randint(1, 10)):
        final_text += new_paragraph(trigrams_words)
        final_text += "\n\n"

    print (final_text)
