from itertools import *

m = []
for x in product('КУПЧИХА', repeat=7):
    s = ''.join(x)
    if s[0] != 'Ч' and s.count('ИАУ') == 0 and len(set(list(map(str, s)))) == 7:
        m.append(s)
print(len(m))
