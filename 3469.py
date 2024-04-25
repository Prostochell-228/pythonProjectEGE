import functools
@functools.lru_cache()
def F(n):
    if n == 0: return 1
    if n > 0:
        return 2 * F(1 - n) + 3 * F(n - 1) + 2
    else:
        return -F(-n)
print(F(50))
