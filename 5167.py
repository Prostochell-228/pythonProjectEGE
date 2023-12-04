import sys
sys.setrecursionlimit(10000)
def F(n):
    if n >= 10000:
        return n
    elif n < 10000 and n % 2 == 0:
        return F(n+2)-3
    elif n < 10000 and n % 2 != 0:
        return F(n+2)+1
print(F(94)-F(80))
