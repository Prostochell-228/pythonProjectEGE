import sys
sys.setrecursionlimit(10000)
def F(n):
    if n>3000:
        return n
    else:
        return F(n+2) + 2
print(F(40) - F(43))