from itertools import *

m = set()
a = product(sorted('0123456789'), repeat=4)

for x in a:
    s = (''.join(x))
    s = s.replace('1', '-')
    s = s.replace('3', '-')
    s = s.replace('5', '-')
    s = s.replace('7', '-')
    s = s.replace('9', '-')
    if s.count('8') <= 2 and '-8' not in s and '8-' not in s and s[0]!='0':
        m.add(x)
print(len(m))
