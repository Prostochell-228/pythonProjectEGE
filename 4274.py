f = open('4274.txt')
a = [int(line) for line in f]
g = []
for i in range(1, len(a) - 1):
    if a[i] < a[i - 1] and a[i] < a[i + 1]:
        g.append(a[i])
print(len(g), max(g))
