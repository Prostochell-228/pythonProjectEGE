f = open('6676.txt')
a = f.readline()
for i in range(72, 91):
    a = a.replace(chr(i), ' ')
a = a.split(' ')
h = []
for i in a:
    h.append(len(i))
print(max(h))
print(sorted(a))