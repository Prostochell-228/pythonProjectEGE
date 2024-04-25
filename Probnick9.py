f = open('Probnick9.csv')
a = [x.split() for x in f]
s = 0
for i in a:
    o = list(map(int, i))
    p = set(map(int, i))
    if len(o) - len(p) == 1:
        h = []
        for j in o:
            h.append(o.count(j))
        l = o[h.index(2)]
        if (sum(p)-l) < l * 2:
            s += 1
print(s)
