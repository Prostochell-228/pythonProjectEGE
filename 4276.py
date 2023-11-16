f = open('4275.txt')
a = [int(line) for line in f]
g = 0
b = a.copy()
b = list(reversed(b))
minc = min(a)
h = b.index(minc)
for i in range(len(a)):
    if a[i] == minc:
        g += 1
print(g, len(a)-h)
