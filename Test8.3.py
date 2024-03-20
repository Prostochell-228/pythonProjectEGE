from itertools import *
m = []
for x in product('МАРT', repeat=6):
    s=''.join(x)
    if s.count('Р')==2:
        m.append(s)
print(len(m))