def F(A):
    for x in range(10000):
        for y in range(10000):
            if not((3*x + 2*y > 25) or (x > 2*y) or (x + 4*y < A)): return True



for i in range(10000):
    if F(i):
        print(i)