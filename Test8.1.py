from itertools import *
m = []
for x in product('ACGT', repeat=5):
    s=''.join(x)
    if s.count('A')==2:
        m.append(s)
print(len(m))