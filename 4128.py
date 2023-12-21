import functools
@functools.lru_cache()
def F(n):
    if n==0: return 0
    elif 3>n>=1: return 1
    elif n>=3:return F(n - 1) + F(n - 2)
print(F(47))