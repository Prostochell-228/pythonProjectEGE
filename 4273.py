f = open('4273.txt')
a = [int(line) for line in f]
g = []
b = []
h = []
for i in range(1, len(a) - 1):
    if a[i] > a[i - 1] and a[i] > a[i + 1]:
        g.append(a[i])
        b.append(i)
for i in range(len(b) - 1):
    h.append(b[i + 1] - b[i])
print(len(g), min(h))
