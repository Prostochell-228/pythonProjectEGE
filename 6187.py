import sys
sys.setrecursionlimit(1000000)

def F(n):
    if n<=2:
        return 5
    else:
        return F(n-2)+n
print(F(23023))