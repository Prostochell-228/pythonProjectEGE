def F(n,m):
 if m == 0:
   d = 1
 else:
   d = n*F(n, m-1)
 return d

for i in range(1,10000000000):
    if 1000>=F(i,2)>=100:
        print(i)