import functools
import sys
sys.setrecursionlimit(1000000000)
@functools.lru_cache()


def F(n, stop):
    if n == stop:return 1
    if n < stop:return 0
    if n>4:
        if n > stop:return F(n - 1, stop) + F(n - 3, stop) + F(n % 4, stop)
    else:
        if n > stop: return F(n - 1, stop) + F(n - 3, stop)



print(F(22, 2))
