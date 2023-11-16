f = open('4275.txt')
a = [int(line) for line in f]
g = 0
maxi = max(a)
h = a.index(maxi) + 1
for i in range(len(a)):
    if a[i] == maxi:
        g += 1
print(g, h)
