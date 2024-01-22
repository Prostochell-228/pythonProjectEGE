import itertools

a = 'abcdefghijkl'
print(len(a))
g = itertools.combinations(a, 7)
g = list(g)
print(len(g))
gg = g.copy()
for i in gg:
    if len(i)!=len(set(i)):
        g=g.remove(i)
print(len(g))
print(g)
