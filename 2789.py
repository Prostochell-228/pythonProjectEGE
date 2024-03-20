from itertools import *

m = []
for i in product('УОА', repeat=5):
    s = ''.join(i)
    m.append(s)
m = sorted(m)[::-1]
print(m[99])