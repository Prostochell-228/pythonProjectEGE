f = open('4270.txt')
a = [int(line) for line in f]
g = []
for i in range(len(a)-1):
    if (abs(a[i]) % 10 == 6 and abs(a[i]) % 3 == 0) or (abs(a[i+1]) % 10 == 6 and abs(a[i+1]) % 3 == 0):
            g.append(min(a[i],a[i+1]))
print(len(g), min(g))
