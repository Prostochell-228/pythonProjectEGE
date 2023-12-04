import sys
sys.setrecursionlimit(10000)

def F(n):
    if n >= 4040:
        return n
    else:
        return n + 4 + F(n + 4)


print(F(3) - F(15))
