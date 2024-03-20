from itertools import *

m = []
for x in product('АОУ', repeat=5):
    s = ''.join(x)
    m.append(s)
print(m.index('ОАААА')  )