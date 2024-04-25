from itertools import *
s=0
for x in product('0123456789ABCDEF', repeat=3):
    x = list(x)
    if len(x)==len(set(x)):
        x=''.join(x)
        for i in '02468ACE':
            x = x.replace(i,'-')
        for i in '13579BDF':
            x = x.replace(i,'*')
        if not('--' in x) and not('**' in x):
            s+=1
print(s)