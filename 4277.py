f = open('4277.txt')
a = [int(line) for line in f]
g = 0
c = []
b = a.copy()
for i in range(1, len(b) - 1):
    if b[i] > b[i + 1]:
        g += 1
    else:
        c.append(g+1)
        g = 0
print(max(c), c.count(max(c)))
