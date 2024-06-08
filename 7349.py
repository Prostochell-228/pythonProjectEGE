f = [x for x in open('7354.csv')]
s = 0
for line in f:
    m = sorted([int(x) for x in line.split()])
    t = 0
    k = 0
    if len(m) != len(set(m)) and m[5] != m[4]:
        h = [m.count(m[0]), m.count(m[1]), m.count(m[2]), m.count(m[3]), m.count(m[4]), m.count(m[5])]
        for i in range(len(h)):
            if h[i] > 1:
                t += m[i]
            else:
                k += m[i]
        if t > k:
            s += 1
print(s)
