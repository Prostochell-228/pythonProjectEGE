import fnmatch
h = []
for i in range(0, 10 ** 10 + 1, 50068):
    if fnmatch.fnmatch(str(i), '9?979*8') == True and '0' in str(i):
        h.append([i,i//50068])
print(h)