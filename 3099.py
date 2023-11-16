f = open('3099.txt')
a = f.readline()
f = []
s = 0
for i in range(65, 91):
    f.append(a.count(chr(i)))
for i in f:
    if i % 2 != 0:
        s += 1
print(s/2)
