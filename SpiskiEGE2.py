def test(x):
    for i in range(2, round(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


def test2(a, x):
    s = 1
    for i in a:
        s*=i
    if x==s:
        return True
    else:
        return False
def test3(a):
    if a[0]%10==a[1]%10 and a[0]%10==a[2]%10:
        return True
    else:
        return False

b = []
a = []
s = 0
for x in range(356712, 420901):
    for i in range(2, round(x ** 0.5) + 1):
        if x % i == 0:
            if test(i):
                a.append(i)
            if test(x // i):
                a.append(x // i)
    if len(a) == 3 and test2(a, x) and test3(a):
        b.append(x)
    a = []
print(len(b), sum(b)/len(b))
