from itertools import *
m = []
for x in product('БАЛКОН', repeat=3):
    s=''.join(x)
    if s.count('Б'):
        m.append(s)
print(len(m))