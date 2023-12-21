f = open('6642.txt')
a = [int(x.replace('\n', '')) for x in f]
b = a.copy()
b.sort()
b = b[::-1]
maxk = 0
print(b)
for i in b:
    if i % 17 == 0:
        maxk = i
        print(i)
        break
h = []
for i in range(len(a) - 1):
    if a[i] + a[i + 1] > maxk:
        h.append(a[i] + a[i + 1])
print(len(h), max(h))