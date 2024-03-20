def F(A):
    for x in range(1, 1000):
        P = (A + x > 700 - A) and ((A % 100 + 100 % x) > 50)
        if P == False: return False
    return True


for A in range(1, 1000):
    if F(A):
        print(A)
