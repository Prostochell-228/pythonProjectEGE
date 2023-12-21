import fnmatch
h = []
for i in range(0, 10 ** 8 + 1, 2025):
    if fnmatch.fnmatch(str(i), '12*34?5') == True:
        h.append([i,i//2025])
