f = open('9-225.csv')
a = [(x.replace(',', ' ')).split() for x in f]
s = 0
for i in a:
    k = []
    for j in i:
        k.append(int(j))
    M = max(k)
    MN = min(k)
    kk = 0
    for l in k:
        if l!=M and l!=MN:
            kk = kk+(l**2)
    if 5-len(set(i))==1 and kk>((MN+M)**2):
        s+=1
print(s)