f = open('9.csv')
a = [x.split() for x in f]
s = 0
for x in a:
    h = []
    j = 0
    k = []
    if len(x) - len(set(x)) == 4:
        for i in set(x):
            o = x.count(i)
            h.append(o)
            if o == 1:
                j += int(i)
            else:
                k.append(int(i))
    if sorted(h) == [1, 1, 2, 4] and (j / 2) >= max(k):
        s += 1
print(s)