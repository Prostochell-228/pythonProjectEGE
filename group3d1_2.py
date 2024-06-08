f = open('day1_3_2.txt')
a = int((f.readline()))
x = sorted([x for x in [int(x) for x in f]])
h = []
s = x[0]
for i in range(1, len(x)):
    if x[i] - s >= 4:
        h.append(s)
        s = x[i]
print(len(h) + 1, h[0])
