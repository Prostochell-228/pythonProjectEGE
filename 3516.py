def F(A):
    for X in range(1, 10000):
        if (not ((X & 13 != 0) and (X & 39 != 0)) or ((X & A != 0) and (X & 13 != 0))):
            return False
    return True


for A in range(1, 1000000):
    if F(A): print(A); break
