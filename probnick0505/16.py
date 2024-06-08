import sys
from functools import *

sys.setrecursionlimit(10000)
@lru_cache()
def f(n):
    if n == 1: return 1
    if n == 2: return 2
    if n > 2: return n * (n - 1) + f(n - 1) - f(n - 2)


print(f(2024) + f(2020) - f(2019))
