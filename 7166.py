from itertools import *
a = product(sorted('ТБДЦЭЕКНЧ'), repeat=6)
n = 0
for x in a:
    s = ''.join(x)
    if n % 2 == 1 and s.count('Е') >= 3 and s[-1] != 'Н' and s[0] != 'Н':
        print(n+1)
        print(s)
        break
    n+=1