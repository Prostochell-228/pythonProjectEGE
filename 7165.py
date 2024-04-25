from itertools import *

m = set()
a = product(sorted('МБНОВШЩУ'), repeat=4)
n = 1
for x in a:
    s = ''.join(x)
    if n % 2 == 1 and s[-1] != 'В':
        m.add(x)
    n += 1
print(len(m))