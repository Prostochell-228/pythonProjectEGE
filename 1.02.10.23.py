def test2(x):
    z = []
    for i in range(2, round(x ** 0.5) + 1):
        if x % i == 0:
            z.append(i)
            z.append(x//i)
    return z

for i in range(154026,154043):
    h = test2(i)
    if len(h)==2:
        print(max(h), i)
