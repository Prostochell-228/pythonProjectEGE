def F(A):
    for x in range(10000):
        a = (A + x < 123) <= ((x % 5 == 0) <= (not (x % 7 == 0)))
        if not (a):
            return False
    return True


for i in range(10000):
    if F(i):
        print(i)
        break
