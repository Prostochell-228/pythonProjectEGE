from itertools import *

m = []
for x in product('НОБЕЛИЙ', repeat=7):
    s = ''.join(x)
    if s[0] != 'Й' and s.count('ИЙО') == 0 and len(set(list(map(str, s)))) == 7:
        m.append(s)
print(len(m))
