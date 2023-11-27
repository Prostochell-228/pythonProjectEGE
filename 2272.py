def F(n):
    if n<=3:
        return n
    else:
        if n%2==0:
            return n + 3 + F(n-1)
        else:
            return n*n + F(n-2)
h = []
for i in range(1,1001):
    gg = F(i)
    if gg%7==0:
        h.append(gg)
print(len(h))
