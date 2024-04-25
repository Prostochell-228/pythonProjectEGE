f = open('14642.txt').readline()
f = f.replace('F', '-')
for i in range(200,1,-1):
    f = f.replace('-'*i, ' ')
f = f.replace('E', 'A')
f = f.replace('D', 'A')
f =f.split()
h = []
for x in f:
    h.append([len(x),x.count('-'),x])
h = sorted(h)
print(h)
for x in h:
    if x[1]==1:
        print(x)