from itertools import *

a = permutations('ГЛУБИНА',7)
k = 0

for i in a:
    s = ''.join(i)
    if s.index('Г')>s.index('И') and s.index('Г')>s.index('А'):
        k+=1
print(k)
