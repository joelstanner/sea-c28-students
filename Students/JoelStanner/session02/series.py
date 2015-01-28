MEMO = {0:0, 1:1}
LUCAS_MEMO = {0:2, 1:1}

def fibonacci(n):
    """Return the nth fibonacci number for input n."""
    if not n in MEMO:
        MEMO[n] = fibonacci(n-1) + fibonacci(n-2)
    return MEMO[n]

def lucas(n):
    """Return the nth lucas number for input n."""
    if not n in LUCAS_MEMO:
        LUCAS_MEMO[n] = lucas(n-1) + lucas(n-2)
    return LUCAS_MEMO[n]
