f = open('day1_13.txt').readline()
for i in 'BEF':
    f = f.replace(i,' ')
f = f.split()
h = []
for i in f:
    h.append(len(i))
print(max(h))