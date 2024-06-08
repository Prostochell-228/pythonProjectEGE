nw = ''

def per(n):
    global nw
    nw = ''
    while n > 0:
        r = n % 8
        nw = str(r) + nw
        n = n // 8
    return nw



def F(i):
    n = per(int(i))
    s = sum(map(int, n))
    if s % 2 == 0:
        g = n[0]
        n = g + n + g
    else:
        g = n[-1]
        n = n + g
    if int(n, 8) < 1100:
        print(i)


for i in range(1,200):
    F(i)
