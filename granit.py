import functools
import sys
sys.setrecursionlimit(1000000000)

def F(n):
    if n<11:
        return n
    else:
        return n+F(n-1)
print(F(2024)-F(2021))