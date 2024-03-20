from itertools import *
m = []
for x in product('КУМА', repeat=5):
    s=''.join(x)
    if (s[0]=='К' or s[0]=='М') and (s[4]=='У' or s[4]=='А'):
        m.append(s)
print(len(m))