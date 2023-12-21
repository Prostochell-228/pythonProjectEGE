f = open('2667b.txt')
l = f.readline()
a = [x.replace('\n','') for x in f]
print(a)
h = []
hh=[]
hhh = []
for n in a:
    n = int(n)
    f = []
    d = 2
    m = n
    while d * d <= n:
        if n % d == 0:
            f.append(d)
            n //= d
        else:
            d += 1
    f.append(n)
    h.append([m, f])
for i in h:
    if i[1].count(7)==1:
        hh.append(i[0])
    if i[1].count(7)==0:
        hhh.append(i[0])
print(max(hh)*max(hhh))
