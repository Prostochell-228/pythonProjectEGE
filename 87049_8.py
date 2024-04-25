from itertools import *
h = 0
a = product('ПРИКАЗ', repeat=4)
for i in a:
    s = ''.join(i)
    if s.count('К')==1:
        h+=1
print(h)