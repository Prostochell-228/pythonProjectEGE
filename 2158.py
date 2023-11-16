f = open('2158.csv')
b = [(line).replace("\n", "") for line in f]
a = []
h = []
for i in b:
    a.append(int(i))
for i in range(0, len(a) - 5):
    b = a.copy()[5 + i:]
    for j in b:
        if sum(map(int, str(j))) + sum(map(int, str(a[i])))<100:
            h.append(j + a[i])
print(len(h))
