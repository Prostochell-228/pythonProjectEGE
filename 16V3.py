import sys
import functools


@functools.lru_cache(None)
def F(n):
    if n == 1: return 1
    if n == 2: return 2
    if n > 2: return n * (n - 1) + F(n - 1) + F(n - 2)

for n in range(3,5000):
    F(n)
    
print(F(2024)-F(2022)-2*F(2021)-F(2020))
