import fnmatch
for i in range(0, 10**10+2, 2024):
    if fnmatch.fnmatchcase(str(i), '1?2157*4'):
        print(i, i/2024)