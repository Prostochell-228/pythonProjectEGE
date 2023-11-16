import itertools
f = open('2666.txt')
b = f.readline()
a = [int(line) for line in f if int(line) % 2 == 0 or int(line) % 3 == 0]
sat = set(a)
permutations = list(itertools.permutations(sat, 2))
for p in permutations:
    print(p)