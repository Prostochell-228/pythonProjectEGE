from itertools import *

m = set()
for x in product('012345678', repeat=5):
    s = ''.join(x)
    if (s[0] in '2468') and (s.count('3') <= 1):
        if (s[-1] not in '18'):
            m.add(s)
print(len(m))
