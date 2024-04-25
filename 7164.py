from itertools import *

m = set()
a = product(sorted('ДОЩГХИМТЭ'), repeat=5)
n = 1
for x in a:
    s = ''.join(x)
    if n % 2 == 0 and s[0] != 'М' and s[0] != 'И':
        m.add(x)
    n += 1
print(len(m))
