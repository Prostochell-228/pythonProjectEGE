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


def test3(a):
    if a[0] % 10 == a[1] % 10 and a[0] % 10 == a[2] % 10:
        return True
    else:
        return False


b = []
a = []
s = 0
for x in range(321654, 654321):
    for i in range(2, round(x ** 0.5) + 1):
        if x % i == 0 and x % 2 != 0:
            a.append(i)
        if x % (x // i) == 0 and (x // i) % 2 != 0:
            a.append(x // i)
    if len(a) > 70:
        b.append([x, max(a)])
    a = []
print(b)
