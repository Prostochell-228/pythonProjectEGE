import sys
import functools
sys.setrecursionlimit(10000000)
@functools.lru_cache(None)
def F(n):
    if n >= 10000:
        return 1
    else:
        if n % 2 == 0:
            return F(n + 3) + 7
        else:
            return F(n+1) - 3


for i in range(10000, 1, -1):F(i)
#заранее просчитанаяя рекурсия


print(F(50)-F(57))