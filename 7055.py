nw = ''
h = []


def per(n):
    global nw
    nw = ''
    while n > 0:
        r = n % 6
        nw = str(r) + nw
        n = n // 6
    return nw


def F(i):
    n = per(int(i))
    if int(n, 6) % 3 == 0:
        g = n[0] + n[1]
        n = n + g
    else:
        n = n + per((int(n, 6) % 3)*10)
    if int(n, 6) > 680:
        h.append(int(n, 6))


for i in range(8, 2000):
    F(i)
print(min(h))
