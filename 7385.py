nw = ''


def per(n):
    global nw
    nw = ''
    while n > 0:
        r = n % 4
        nw = str(r) + nw
        n = n // 4
    return nw


def F(i):
    n = per(int(i))
    if i % 2 == 0:
        g = n[-2] + n[-1]
        n = n + g
    else:
        n = n + per(int((i % 4) * 5))
    if int(n, 4) < 555:
        print(i)


for i in range(8, 2000):
    F(i)
