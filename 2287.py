def F(n):
    if n<=18:
        return n+3
    else:
        if n%3==0:
            return (n//3)*F(n//3) + n - 12
        else:
            return F(n-1) + n*n + 5
h = []
for i in range(1,801):
    gg = F(i)
    k = True
    ggg = list(map(int, str(gg)))
    for i in ggg:
        if i%2!=0:
            k = False
    if k:
        h.append(gg)
print(len(h))