from itertools import *
m = []
for x in product('ТОК', repeat=6):
    s=''.join(x)
    if s[0]=='Т' or s[0]=='К':
        m.append(s)
print(len(m))