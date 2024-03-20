from itertools import *

m = []
for x in product('КОМПЬЮТЕР', repeat=5):
    s = ''.join(x)
    if s[0] not in 'Ь' and s.count('К') == 2:
        m.append(s)

print(sorted(set(m)).index([sorted(set(m))[x] for x in range(1, len(m), 2)][-1]))
