import fnmatch
for i in range(98591, 10**10+1, 98591):
    if fnmatch.fnmatch(str(i),'5?2*3?3?')==True:
        print(i, i//98591)