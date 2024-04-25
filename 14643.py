f = open('14643.txt').readline()
f = f.replace('AXMM', ' ')
f =  f.split()
h = []
for x in f:
    h.append(len(x))
print(max(h))