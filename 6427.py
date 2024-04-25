from fnmatch import *
a =[]
for i in range(12480, 10**7+1):
    g = str(i)
    if fnmatch(g, '12*4*8?'):
        print()