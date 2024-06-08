import sys

sys.setrecursionlimit(10000)


def F(n):
    if n >= 1300: return n
    if n < 1300:
        if n % 2 != 0:
            return n * F(n + 1)
        else:
            return n * F(n + 2) / 4


print(F(1286) / F(1290))
