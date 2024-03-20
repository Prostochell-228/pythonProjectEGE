def F(A):
    for x in range(10000):
        for y in range(10000):
            a = (x*y<A) or (x<y) or (9<x)
            if not(a): return False
    return True
for i in range(10000):
    if F(i):
        print(i)
        break