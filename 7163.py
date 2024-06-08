from itertools import *

a = product(sorted('СКОЕМЧ'), repeat=5)
j =0
for x in a:
    s = ''.join(x)
    j += 1
    if s[0]=='Ч' and s[-1]=='О' and j:
        print(j)

