def ch(n):
    s = ''
    while n > 0:
        r = n % 4
        s = str(r) + s
        n = n // 4
    return s


def f(n):
    i = ch(n)
    if n % 4 == 0:
        j = i[-2] + i[-1]
        i = i + j
    else:
        j = ch((n % 4) * 2)
        i = i + j
    print(int(i, 4))
    return (int(i, 4))

for i in range(16,200):
    if f(i)>=1088:
        print(i)
        break
