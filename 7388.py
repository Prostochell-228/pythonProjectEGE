import sys
sys.setrecursionlimit(10000)
def F(n):
    if n==1: return 1
    if n>1: return 3*n + 2 + F(n - 1)
print(F(2024) - F(2020))