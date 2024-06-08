f = open('13394.txt')
b = int(f.readline())
a = [int(x) for x in f]
h = []
l = []
for i in a:
    if i > 350:
        h.append(i)
    else:
        l.append(i)
h.sort()
s1 = sum(h[0:len(h) // 3]) * 0.75
print(sum(h) + sum(l) - s1)
h.sort(reverse=True)
s2 = 0
print(h)
for i in range(len(h)):
    if i % 3 == 2:
        c = h[i - 2] + h[i - 1] + h[i] * 0.25
        if c == int(c):
            s2 += int(c)
        else:
            s2 += (int(c) + 1)
print(len(h) % 3)
print(s2+sum(l))