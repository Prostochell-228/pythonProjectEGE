from itertools import *
m = []
for x in product('ТОК', repeat=6):
    s=''.join(x)
    if s[0]!='Й' and s[0]=='К':
        m.append(s)
print(len(m))