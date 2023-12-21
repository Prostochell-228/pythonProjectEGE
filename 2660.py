f = open('2660a.txt')
l = f.readline()
a = [x.replace('\n','').split() for x in f]
h = []
for i in range(len(a)):
    k=[0]
    if sum(map(int,(a[i])[0]))%3!=0:
        k.append(int((a[i])[0]))
    if sum(map(int,(a[i])[1]))%3!=0:
        k.append(int((a[i])[1]))
    h.append(max(k))
print(sum(h))