from itertools import *

m = []
for x in product('012345678', repeat=5):
    s = ''.join(x)
    if '6' in s:
        if s.index('6') != 0 and s.index('6') != 4:
            if (s.count('6') == 1) and (s[s.index('6') + 1] in '24680') and (s[s.index('6') - 1] in '24680'):
                m.append(s)
        if s.index('6') == 0:
            if (s.count('6') == 1) and (s[s.index('6') + 1] in '24680'):
                m.append(s)
        if s.index('6') == 4:
            if (s.count('6') == 1) and (s[s.index('6') - 1] in '24680'):
                m.append(s)
print(len(m))
