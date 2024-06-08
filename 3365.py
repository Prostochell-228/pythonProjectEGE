f = open('1-2.txt')
a = f.readline()
a = [ord(x) for x in a]
for  i in range(1, len(a)-1):
    print()