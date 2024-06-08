f = open('day1_14.txt').readline()
for i in 'AE':
    f = f.replace(i,' ')
f = f.split()
h = []
for i in f:
    h.append(len(i))
print(max(h))