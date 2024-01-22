from collections import Counter

h = []
for i in range(int(input())):
    h.extend(input().split())

c = Counter(h)
s = [(-a[1], a[0]) for a in h.most_common()]
ss = [a[1] for a in sorted(s)]
print(ss)