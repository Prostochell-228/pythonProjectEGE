from itertools import *

m = []
for x in product('АИОЭУ', repeat=6):
    s = ''.join(x)
    m.append(s)

print(sorted(m).index('ОЭЭЭЭО'))
