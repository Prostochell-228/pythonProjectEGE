from itertools import *

m = []
for i in permutations('НИГРОЛ', 6):
    s = ''.join(i)
    if 'ОИГ' not in s and s[0]!='О':
        m.append(s)
print(len(m))
