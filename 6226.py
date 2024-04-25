from itertools import *

m = []


def F(n):
    h = []
    for i in range(2, round(n ** 0.5) + 1):
        if n % i == 0:
            h.append(i)
            h.append((n // i))
    return h


for i in range(5):
    for x in product('0123456789', repeat=i):
        m.append(''.join(x))
res = []
for a in '0123456789':
    for b in '0123456789':
        for c in m:
            for d in m:
                N = int(f'1{a}2{c}0{d}2{b}1')
                h = F(N)
                if len(h)==3:
                    print(N,max(h))
