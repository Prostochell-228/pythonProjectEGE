f = open('4271.txt')
a = [int(line) for line in f]
g = []
for i in range(len(a) - 1):
    if (abs(a[i]) % 9 == 0 and abs(a[i + 1]) % 8 == 3 and abs(a[i + 1]) % 9 != 0) or (
            abs(a[i]) % 8 == 3 and abs(a[i + 1]) % 9 == 0 and abs(a[i]) % 9 != 0):
        g.append(max(a[i], a[i + 1]))
print(len(g), max(g))
