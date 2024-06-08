import sys

sys.setrecursionlimit(10000)


def F(n):
    if n >= 10000: return n
    if n < 10000:
        if n % 2 == 0:
            return F(n + 2) - 3
        else:
            return F(n + 2) + 1


print(F(9994) - F(9980))
