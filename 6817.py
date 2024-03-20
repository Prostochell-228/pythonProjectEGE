from itertools import *

m = []
for i in permutations('0123456789ABCDEF', 3):
    s = ''.join(i)
        #m.append(s)
print(len(m))
