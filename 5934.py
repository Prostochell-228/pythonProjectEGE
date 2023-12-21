import fnmatch

for i in range(124579, 10 ** 8 + 1):
    if fnmatch.fnmatch(str(i), '124*5*79') == True:
        sc = 0
        for x in str(i):
            if x in '13579':
                sc += int(x)
            if i % sc == 0:
                print(i, sum([int(x) for x in str(i)]))
                