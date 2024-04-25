f = open('13715.txt').readline()
f = f.replace('AB', 'a1b')
s = 0
ss = 0
h = []
for x in f:
    ss += 1
    if x == '1':
        s += 1
    if s==50:
        h.append(ss)
        s=0
        ss=0
print(max(h))