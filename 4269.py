f = open('4269.txt')
a = [int(line) for line in f]
g = []
for i in range(len(a)-1):
    if (a[i] % 7 == 0 and a[i + 1] % 17 != 0) or (a[i] % 17 and a[i + 1] % 7 == 0):
            g.append(a[i]+a[i+1])
print(len(g), min(g))
