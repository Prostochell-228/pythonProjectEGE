f = open('3782.txt')
a = [str(line) for line in f]
h1 = []
h3 = []
s = 0
for i in a:
    h1.append(i.count("Q"))
h2 = h1[::-1]
gg = h2.index(max(h1))
numm = h1.index(h1[-gg - 1])
for i in range(65, 91):
    j = a[numm].count(chr(i))
    h3.append(j)
print(h3)
k = chr(65 + h3.index(min(h3)))
for i in a:
    s += i.count(k)
print(k, s)
