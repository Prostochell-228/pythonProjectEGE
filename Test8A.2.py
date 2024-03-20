from itertools import *

m = []
for x in product('АКРУ', repeat=5):
    s = ''.join(x)
    m.append(s)
print(m[250])
