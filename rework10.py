def test(n):
    for i in range(2, round(n ** 0.5) + 1):
        if n % i == 0:
            return 0
    return 1


def rr(n):
    h = []
    for i in range(2, round(n ** 0.5) + 1):
        if n % i == 0 and test(i):
            h.append(i)
            if test(n // i):
                h.append(n // i)
    return sum(h)


for i in range(33333, 55556):
    d = rr(i)
    if d > 250 and i % 250 == 0:
        print(i)
