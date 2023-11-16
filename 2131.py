a = 912673
h = []


def delnatehree(a):
    s = 0
    j = []
    for i in range(103, 994, 10):
        if a % i == 0:
            j.append(i)
            s += 1
        if s > 3:
            return 0
    if s<3:
        return 0
    else:
        return min(j)

while len(h) < 5:
    a += 1
    k = delnatehree(a)
    if k!=0:
        h.append([a,k])
print(h)
