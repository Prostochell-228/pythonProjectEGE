from itertools import *

a = product(sorted('БЭПН'), repeat=4)
s = 0
for i in a:
    s+=1
    if i[0] != 'П' and i[-1] != 'П' and 'ЭЭ' not in (''.join(i)):
        print(s)
