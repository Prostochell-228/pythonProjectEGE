from itertools import *

m = []
for x in product('УДАЧА', repeat=5):
    s = ''.join(x)
    if s[0] in 'УА':
        m.append(s)

print(sorted(set(m)).index('УДАЧА'))
