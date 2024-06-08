f = [x for x in open('7354.csv')]
m = []
s = 0
a = [[] for i in range(6)]
for line in f:
    m = [int(x) for x in line.split()]
    for i in range(len(m)):
        a[i].append((m[i]))
for line in f:
    t = 0
    m = [int(x) for x in line.split()]
    for i in range(len(m)):
        if m.count(m[i]) == 1 and a[i].count(m[i]) < 170:
            t += 1
    if t>4:
        s += 1
print(s)
