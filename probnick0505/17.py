a = [int(x) for x in open('17var04.txt')]
b = a.copy()
j = None
h = []
for i in sorted(b):
    k = str(i)
    if (k[-3] + k[-2] + k[-1]) == '700':
        j = i
        break
for i in range(len(a) - 2):
    if sum([a[i], a[i + 1], a[i + 2]]) >= j and (str(len(str(abs(a[i])))) + str(len(str(abs(a[i + 1])))) + str(len(str(abs(a[i + 2]))))).count('5') <= 2:
        h.append(sum([a[i], a[i + 1], a[i + 2]]))
print(len(h), min(h))
