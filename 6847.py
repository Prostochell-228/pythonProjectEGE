from math import ceil, sqrt


def simple(x):
    for i in range(2, ceil(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def gett(num):
    f = [x for x in range(1, ceil(sqrt(num)) + 1) if num % x == 0]

    s = [int(num / x) for x in reversed(f) if int(num / x) not in f]

    return f + s

# 6869 1717
g = gett(12345)
s = []
for i in g:
    if simple(i):
        s.append(i)
print(s)
