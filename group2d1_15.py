f = open('day1_16.txt').readline()
for i in 'QWERTYUIOPASDFGHJKLZXCVBNM':
    f = f.replace(i,' ')
f = f.split()
h = []
for i in f:
    if int(i)%2==0:
        h.append(int(i))
print(max(h))
print(sorted(h))