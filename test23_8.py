from itertools import *

a = 'КБР'
b = 'ОУА'
s = 0
for i in permutations('КОБУРА', 6):
    i = ''.join(i)
    for j in a:
        i = i.replace(j, '-')
    for j in b:
        i = i.replace(j, '*')
    if '-*-*-*' in i or '*-*-*-' in i:
        s += 1
print(s)
