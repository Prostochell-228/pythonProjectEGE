import functools
import sys
sys.setrecursionlimit(10000)
def F(n):
    if n<=2:
        return n
    else:
        return n + F(n - 2)
print(F(2023) + F(2020))
