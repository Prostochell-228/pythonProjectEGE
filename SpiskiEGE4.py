def test(x):
    for i in range(2, round(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


def test2(a, x):
    s = 1
    for i in a:
        s *= i
    if x == s:
        return True
    else:
        return False


b = []
a = []
s = 0
for x in range(25317, 51237):
    for i in range(2, round(x ** 0.5) + 1):
        if x % i == 0:
            if test(i):
                a.append(i)
            if test(x // i):
                a.append(x // i)
    if len(a) == 6 and test2(a, x):
        b.append([x, max(a)])
    a = []
print(b)
