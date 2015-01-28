"""Series.py from session02 task2"""

MEMO = {0: 0, 1: 1}
LUCAS_MEMO = {0: 2, 1: 1}


def fibonacci(n):
    """Return the nth fibonacci number for input n."""
    if n < 0:
        return None
    elif n not in MEMO:
        MEMO[n] = fibonacci(n-1) + fibonacci(n-2)
    return MEMO[n]


def lucas(n):
    """Return the nth lucas number for input n."""
    if n < 0:
        return None
    if n not in LUCAS_MEMO:
        LUCAS_MEMO[n] = lucas(n-1) + lucas(n-2)
    return LUCAS_MEMO[n]


def sum_series(n, first=0, second=1):
    """Return the nth series number for input n.

    n = nth number in the series
    first=0 : starting number in the series.
    second=1 : second nubmer in the series.

    first=0, second=1 : Fibonacci series
    first=2, second=1 : Lucas series
    """
    if n < 0:
        return None
    if n == 0:
        return first
    elif n == 1:
        return second
    else:
        return (
            sum_series(n-1, first, second) + sum_series(n-2, first, second)
        )

if __name__ == '__main__':
    # testing

    # negative numbers return None
    assert fibonacci(-1) is None
    assert fibonacci(-123) is None

    # normal numbers
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13

    # lucas tests
    assert lucas(-1) is None
    assert lucas(-123) is None

    assert lucas(0) == 2
    assert lucas(1) == 1
    assert lucas(2) == 3
    assert lucas(3) == 4
    assert lucas(4) == 7
    assert lucas(5) == 11
    assert lucas(6) == 18
    assert lucas(7) == 29

    # sum_series tests (check for fibonacci and lucas equality)
    assert sum_series(-1) is None
    assert sum_series(-123) is None

    assert sum_series(2) == fibonacci(2)
    assert sum_series(7) == fibonacci(7)

    assert sum_series(2, 2, 1) == lucas(2)
    assert sum_series(7, 2, 1) == lucas(7)

    print("All Tests Passed")
