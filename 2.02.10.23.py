def test2(x):
    z = []
    for i in range(2, round(x ** 0.5) + 1):
        if x % i == 0:
            if i%2==0:
                z.append(i)
            if (x//i)%2==0:
                z.append(x//i)
    return z

for i in range(190201,190260):
    h = test2(i)
    if i%2==0:
        h.append(i)
    h = sorted(h)
    if len(h)==4:
        print(h[-2], h[-1])
