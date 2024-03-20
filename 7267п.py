def F(A):
    for x in range(10000):
        for y in range(10000):
            if not((4 * x + y > 115) or (x > 3 * y) or (x + 4 * y < A)): return True



for i in range(10000):
    if F(i):
        print(i)
