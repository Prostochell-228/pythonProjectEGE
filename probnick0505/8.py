from itertools import *

a = sorted(list(product(sorted('ИНТЕГРАЛ'), repeat=5)))
s = 0
for i in range(0, len(a), 2):
    if (a[i])[0] != 'Т' and (a[i].count('Н') == 1 or a[i].count('Н') == 2):
        s += 1
print(s)

