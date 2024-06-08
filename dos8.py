from itertools import *
h = []
a = product(sorted('АПРСУ'), repeat=5)
for x in list(a):
    k = (''.join(x)).replace('А', '-')
    if not('--' in k) and k.count('У')<=1:
        h.append(1)
    else:
        h.append(0)
print(h.index(1), len(h), h[129], h[130])