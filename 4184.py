import itertools
f = open('4184.txt')
a = f.readline()
my_list = 'QWERTYUIOPASDFGHJKLZXCVBNM'
permutations = list(itertools.permutations(my_list, 3))
j = permutations.copy()
s = 0
h = []
for i in range(0, len(a)-2, 3):
    if a[i] + a[i + 1] + a[i + 2] in j:
        h = (a[i], a[i + 1], a[i + 2])
        j.remove(h)
        s += 1
    else:
        h.append(s)
        s = 0
        j = permutations.copy()
print(max(h))