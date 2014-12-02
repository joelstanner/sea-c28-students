from __future__ import print_function

def fibonacci(n):
    """Return the nth value of the Fibonacci series."""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
