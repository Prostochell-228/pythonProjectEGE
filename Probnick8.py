from itertools import *

global hb
global ha
a = permutations('13579BDF', 2)
ha = []
for i in list(a):
    ha.append(i[0] + i[1])
b = permutations('02468ACE', 2)
hb = []
for i in list(b):
    hb.append(i[0] + i[1])


def F1(h):
    for i in ha:
        if i in h:
            return False
    return True


def F2(h):
    for i in hb:
        if i in h:
            return False
    return True


s = 0
for i in range(256, 4095 + 1):
    h = hex(i)[2::]
    if len(set(map(str, h))) == len(h) and F1(h) and F2(h):
        s += 1
print(s)
