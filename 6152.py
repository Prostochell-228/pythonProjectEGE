from fnmatch import *

h = []
for i in range(0,10 ** 9 + 1, 28):
    if fnmatch(str(i), '6323*353?'):
        h.append([i, i // 28])
        print(i)
print(sorted(h)[::-1])
