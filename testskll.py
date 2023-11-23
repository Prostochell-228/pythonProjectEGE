def d11(a, b): return a + b


def d12(a, b): return max(a, b)  # ??????


def d13(a):
    if a == 1:
        return 1
    return d13(a - 1) * a


def d14(i):
    for a in range(2, round(i ** 0.5) + 1):
        if i % a == 0:
            return False
    return True


def d15(i):
    if i == i[::-1]:
        return True
    return False


def d16(i): return len(str(i))


def d17(i):
    h = []
    for a in range(1, round(i ** 0.5) + 1):
        if i % a == 0:
            h.append(a)
            h.append(i // a)
    return h


def d18(k):
    N = len(k)
    for i in range(N - 1):
        for j in range(N - i - 1):
            if k[j] > k[j + 1]:
                b = k[j]
                k[j] = k[j + 1]
                k[j + 1] = b
    return k


def d19(a, b):
    h = []
    for i in range(a, b + 1):
        if d14(i):
            h.append(i)
    return h


def d20(a, b):
    h1 = set(a)
    h2 = set(b)
    j1 = []
    j2 = []
    for i in h1:
        j1.append(a.count(i))
    for i in h2:
        j2.append(b.count(i))
    if h1 == h2 and j1 == j2:
        return True
    else:
        return False


def r1(n):
    if n > 1:
        r1(n - 1)
    print(n)


def r2(n):
    if n == 1:
        return 1
    return n + r2(n - 1)


def r3(n, b):
    if n == 0:
        return n
    else:
        return (b % n)


l = []


def r4(n):
    if (n == 0):
        return l
    dig = n % 10
    l.append(dig)
    r4(n // 10)


def r5(n):
    if n in (1, 2):
        return 1
    return r5(n - 1) + r5(n - 2)
