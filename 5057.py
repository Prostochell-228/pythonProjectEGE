f = open('5057.txt')
a = [int(x.replace('\n', '')) for x in f]
b = a.copy()
b.sort(reverse=True)
h = []
for i in b:
    if i % 41 == 0:
        b = i
        break
for i in range(len(a) - 1):
    s = a[i] + a[i+1]
    if s < b:
        h.append(s)
print(len(h), max(h))

