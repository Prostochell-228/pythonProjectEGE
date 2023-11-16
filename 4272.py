f = open('4272.txt')
a = [int(line) for line in f]
g = []
for i in range(1, len(a)):
    if a[i] > a[i - 1]:
        g.append(abs(a[i] - a[i - 1]))
print(len(g), min(g))
