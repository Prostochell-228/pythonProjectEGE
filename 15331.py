import sys
sys.setrecursionlimit(10000)
def F(n):
    if n<=7:
        return 1
    else:
        return n+2+F(n-1)
print(F(2024)-F(2020))