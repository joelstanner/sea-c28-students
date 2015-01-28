def ack(m, n):
    """Return the value of the Ackermann function for inputs m, n."""
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ack(m-1, 1)
    elif m > 0 and n > 0:
        return ack(m-1, ack(m, n-1))
    else:
        return None


if __name__ == '__main__':
    for m in range(0, 4):
        for n in range(0, 5):
            print("m is " + str(m) + " n is " + str(n) +
                  " = " + str(ack(m, n)))
