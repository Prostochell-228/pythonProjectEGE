f = open('87049_9.csv')
a = [x.split() for x in f]
h = 0
for i in a:
    s = []
    for j in i:
        s.append(int(j))
    ss = sorted(s)
    print(ss)
print(h)
