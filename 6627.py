from itertools import *

s = 0
f = open('6627.csv')
for i in [(x.replace('\n', '')).split() for x in f]:
    h = sorted([int(i[0]), int(i[1]), int(i[2]), int(i[3])])
    a = [h[3] - h[0], h[2] - h[1]], [h[1] - h[0], h[3] - h[2]], [h[3] - h[2], h[1] - h[0]]
    if (h[0] + h[3]) % 3 == 0:
        for j in a:
            if j[0] == j[1]:
                s += 1
                break
print(s)
