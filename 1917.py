from itertools import *
m = []
for x in product('ГЕРОЙ', repeat=4):
    s=''.join(x)
    if s[0]!='Й' and (s.count('Е')>0 or s.count('О')>0):
        m.append(s)
print(len(m))