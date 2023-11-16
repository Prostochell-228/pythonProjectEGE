from math import sqrt


def test(x):
    for i in range(2, round(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


h = 0
for i in range(round(sqrt(3661)), round(sqrt(33625))):
    if test(i):
        h+=1
print(h)
