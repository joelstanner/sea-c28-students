#!/usr/bin/env python

"""
Generators for:

Sum of integers
Doubler
Fibonacci sequence
Prime numbers

"""


def intsum():
    """Generates numbers that are in the sequence 0 + 1 + 2 + 3 + 4 + 5 +
    """
    i = 0
    sum = 0
    while True:
        yield sum
        i += 1
        sum = sum + i

 


def intsum2():
    """Generates numbers that are in the sequence 0 + 1 + 2 + 3 + 4 + 5 +
    """
    i = 0
    sum = 0
    while True:
        sum = sum + i
        i += 1
        yield sum


def doubler():
    """Generates numbers where each value doubles the last value
    """
    i = 1
    while True:
        yield i
        i *= 2


def fib():
    """Generates numbers in a fibonacci sequence: f(n) = f(n-1) + f(n-2)
    """
    n = 1
    m = 0
    while True:
        sum = n + m
        m = n
        n = sum
        yield m


def prime():
    """Generates prime numbers: 2, 3, 5, 7, 11, 13, 17, 19, 23...
    """
    n = 1
    while True:
        n += 1
        if not [i for i in range(2, n) if n % i == 0]:
            yield n


def square():
    """Generates a sequence of squares.
    """
    n = 1
    while True:
        square = n ** 2
        n += 1
        yield square


def everythirdpowerofthree():
    """Generates a sequence every third number to the third power.
    """
    n = 1
    while True:
        square = n ** 3
        n += 1
        if n % 3 == 1:      
            yield square

if __name__ == "__main__":

    g = everythirdpowerofthree()
    for i in range(10):
        print g.next()
