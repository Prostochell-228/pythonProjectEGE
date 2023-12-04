import sys

sys.setrecursionlimit(1000000000)


def F(n):
    if n < 10:
        return n
    elif n % 2 == 0:
        return F(n % 10) + F(n // 10)
    else:
        return F(10 ** n) + F(n % 10) - 2


for i in range(1, 100):
    if F(i) == 0:
        print(i)
h = 0
for l in range(0, 12):
    h+=9*10**(l)
print(h)