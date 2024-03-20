def F(A):
    for x in range(10000):
        for y in range(10000):
            a = (x>=11) or (3*x < y) or (x*y < A)
            if not(a): return False
    return True
for i in range(10000):
    if F(i):
        print(i)
        break