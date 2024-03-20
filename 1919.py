from itertools import *

m = []
for i in permutations('ВОРОТА', 6):
    s = ''.join(i)
    s = s.replace('А', '*')
    s = s.replace('О', '*')
    if '**' not in s:
        m.append(s)
print(len(m))
