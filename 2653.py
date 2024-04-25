from itertools import *

f = open('2653.txt')
n = int(f.readline())
a = [int(x) for x in f]
a = sorted(a)
b = set(a)
w = [0] * (sum(a) + 1)
s = 0
for x in a:
    w2 = w.copy()
    for i in range(s + 1):
        if w[i] == 1:
            w2[i + x] = 1
    w2[x] = 1
    w = w2
    s +=x
k, m = 0, 0
for i in range(sum(a) + 1):
    if w[i] == 0:
        k += 1
        m = i
print(k,m)
