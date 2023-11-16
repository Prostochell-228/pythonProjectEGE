def primfacs(n):
   i = 2
   primfac = []
   while i * i <= n:
       while n % i == 0:
           primfac.append(i)
           n = n / i
       i = i + 1
   if n > 1:
       primfac.append(n)
   return primfac
for k in range(1850000000):
    y = primfacs(1850000000 + k)
    dvc = y.count(2)
    sty = set(y).remove(2) #сет пустой
    j = []
    jj = []
    for i in sty:
        if y.count(i)%2==0:
            j.append(True)
            jj.append(y.count(i))
        else:
            j.append(False)
    sorted(j)
    if dvc%2!=0 and j[0]:
        g = dvc
        for i in jj:
            g+=i
    print(g, k)




