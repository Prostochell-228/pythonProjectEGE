f = open('6539.csv')
a = [x.split() for x in f]
s = 0
for i in a:
    h = []
    for j in i:
        h.append(int(j))
    h = sorted(h)
    if len(set(h)) == len(h) and (h[0] + h[4]) // 2 == (h[1] + h[3]) // 2 and (h[0] + h[4]) // 2 == h[2]:
        s += 1
print(s)