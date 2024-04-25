from itertools import *

a = product('0123456789', repeat=5)
k = 0

for i in a:
    s = ''.join(i)
    for j in '13579':
        s = s.replace(j, '^')

    if s.count('2')==1 and s[0] != '0':
        if s.index('2') == 0 and '2^' in s:
            k += 1
        if s.index('2') == 4 and '^2' in s:
            k += 1
        if '^2^' in s and s.index('2') in [1, 2, 3]:
            k += 1
print(k)
