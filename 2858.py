b = []
a = []
s = 0
for x in range(135790, 163228):
    for i in range(2, round(x ** 0.5) + 1):
        if x % i == 0:
            a.append(i)
            a.append(x // i)
    if sum(a)>460000:
        b.append([len(a), sum(a)])
    a = []
print(b)