f = open('2159.csv')
b = [(line).replace("\n", "") for line in f]
a = []
h = []
ch = []
nech = []
for i in b:
    a.append(int(i))
for g in a:
    if g%2==0:
        ch.append(g)
    else:
        nech.append(g)
for i in range(0, len(a)-9):
    b = a.copy()[9 + i:]
    for j in b:
        if a[i]%2==0 and j in nech:
            h.append(j+a[i])
        elif a[i]%2!=0 and j in ch:
            h.append(j+a[i])
print(len(h))