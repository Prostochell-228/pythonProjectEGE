def F(n):
    if n<=0:
        return 6
    else:
        if n%2==0:
            return 1+F(n/2)
        else:
            return F(n//2)
s = 0
for i in range(1,100):
    if F(i)==9:
        s+=1
print(s)
