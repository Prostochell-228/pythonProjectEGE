import sys
import functools

sys.setrecursionlimit(10000000)
@functools.lru_cache()
def F(n,stop,k):
    if k>7: return 0
    if n<=0:
        return 0
    if k==7:
        if n==stop:
            return 1
        else:
            return 0
    if True: return F(n-5,stop,k+1)+F(n+2,stop,k+1)+F(n**2, stop,k+1)
print(F(3,28,0))