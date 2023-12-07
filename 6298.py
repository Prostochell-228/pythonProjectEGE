def F(a, b):
    if b == 0:
        return a
    if a >= b > 0:
        return F(a - b, b)
    if a < b:
        return F(b, a)
s=0
for i in range(100000000,200000001):
    if i%3!=0 and i%5!=0 and i%7!=0:
        s+=1
print(s)