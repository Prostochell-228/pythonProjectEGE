f = open('2642.txt')
b = f.readline()
a = [int(line) for line in f]
g = sorted(a)
gg = []
ggg = 0
a = sorted(a)[::-1]
j = 30
o = 10
for i in range(o):
    gg.append(a[i])
for i in range(j):
    ggg+=g[i]
print(min(gg))
print(ggg//j)