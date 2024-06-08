def per(n):
    nw = ''
    while n > 0:
        r = n % 3
        nw = str(r) + nw
        n = n // 3
    return nw


def F(n):
    i = per(n)
    if sum(map(int, i)) % 3 == 0:
        i = '20' + i
    else:
        i = '10' + i
    if int(i, 3) < 100:
        print(n)


for i in range(200):
    F(i)
