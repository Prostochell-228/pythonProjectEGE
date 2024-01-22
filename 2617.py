f = open('2617.txt')
s, n = map(int, f.readline().split())
a = [int(x) for x in f]
kol = []
a.sort()
for x in a:
    if sum(kol) + x <= s:
        kol.append(x)
delta = kol[-1] + (s - sum(kol))
for x in a:
    if x <= delta:
        kol[-1] = x
print(len(kol), kol[-1])
