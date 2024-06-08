f = open('day1_17.txt').readline()
f = f.replace('()','-')
f = f.replace('(',' ')
f = f.replace(')',' ')
f = f.split()
h = []
for i in f:
    h.append(len(i))
print(max(h))
print(sorted(h))