f = open('11940.txt')
g = f.readline()
a = []
for x in f:
    k = (x.split())
    a.append([int(k[1]), int(k[0])])
print(sorted((a)))