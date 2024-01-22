import sys
sys.setrecursionlimit(10000000)
def F(n):
    if n==1: return 1
    if n>1:
        return n*F(n-1)+1
print(F(3303)/F(3300))

def F2(n):
    if n==1: return 1
    if n>1:
        return n*F2(n-1)-1
print(F2(1000)/F2(997))