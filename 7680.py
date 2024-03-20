def F(A):
    for x in range(10000):
        for y in range(10000):
            a = (x + 2 * y != 58) or ((A - x > 0) == (A + y > 0))
            if not (a): return False
    return True


for i in range(10000):
    if F(i):
        print(i)
        break
