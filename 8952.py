def F(A):
    for x in range(10000):
        a = ((x & 103 == 0) and (x & 94 != 0)) <= (x & A != 0)
        if not (a):
            return False
    return True


for i in range(10000):
    if F(i):
        print(i)
        break
