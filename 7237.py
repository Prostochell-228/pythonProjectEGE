import sys
sys.setrecursionlimit(10000)
def F(n):
    if n>=1900: return n
    if n<1900:
        if n%3==0:
            return n * F(n + 2) / 3
        else:
            return n * F(n + 1)
print(F(1875) / F(1880))
