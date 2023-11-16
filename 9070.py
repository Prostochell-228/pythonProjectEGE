f = open('9070.txt')
a = [int(line) for line in f]
lev = list(reversed(a[2500:]))
prav = a[:2500]
h = []
print(sorted(a))
for i in range(len(lev)):
    if (prav[i] * lev[i]) % 104 == 0:
        h.append(prav[i] + lev[i])
print(len(h), min(h))
